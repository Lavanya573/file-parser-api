from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db import transaction
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
import threading
import time
import csv
import io
import logging

from .models import File
from .serializers import FileSerializer


logger = logging.getLogger(__name__)

def _simulate_parse_and_extract(file_instance_id: str) -> None:
    try:
        file_obj = File.objects.get(id=file_instance_id)
        # Update to processing
        file_obj.status = 'processing'
        file_obj.progress = 10
        file_obj.save(update_fields=['status', 'progress', 'updated_at'])

        # Read file content from storage
        stored_file = file_obj.file
        parsed_rows = []

        # For demo: if file is CSV, parse via csv module; else, simulate
        if stored_file.name.lower().endswith('.csv'):
            # Ensure text mode for csv module
            with stored_file.open('rb') as fbin:
                with io.TextIOWrapper(fbin, encoding='utf-8', newline='') as f:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                    total = len(rows) if rows else 1
                    for index, row in enumerate(rows, start=1):
                        parsed_rows.append(row)
                        # Increment progress up to 95%
                        new_progress = 10 + int(85 * index / total)
                        if new_progress > file_obj.progress:
                            File.objects.filter(id=file_instance_id).update(progress=new_progress)
        else:
            # Non-CSV: just simulate some processing steps
            for step in range(1, 11):
                time.sleep(0.1)
                new_progress = 10 + step * 8
                File.objects.filter(id=file_instance_id).update(progress=new_progress)

        # Save parsed content
        file_obj.refresh_from_db()
        file_obj.parsed_content = parsed_rows if parsed_rows else {'message': 'Parsed successfully'}
        file_obj.status = 'ready'
        file_obj.progress = 100
        file_obj.save(update_fields=['parsed_content', 'status', 'progress', 'updated_at'])
    except Exception:
        logger.exception("Background parsing failed for file_id=%s", file_instance_id)
        File.objects.filter(id=file_instance_id).update(status='failed')


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('-created_at')
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        upload = request.FILES.get('file')
        if not upload:
            return Response({'detail': 'file is required'}, status=status.HTTP_400_BAD_REQUEST)

        name = request.data.get('name') or upload.name

        with transaction.atomic():
            file_instance = File.objects.create(
                name=name,
                file=upload,
                status='uploading',
                progress=1,
            )

        # Kick off background parsing
        threading.Thread(target=_simulate_parse_and_extract, args=(str(file_instance.id),), daemon=True).start()

        serializer = self.get_serializer(file_instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        file_instance = self.get_object()
        return Response({
            'file_id': str(file_instance.id),
            'status': file_instance.status,
            'progress': file_instance.progress,
        })

    def retrieve(self, request, *args, **kwargs):
        file_instance = self.get_object()
        if file_instance.status != 'ready':
            return Response({'message': 'File upload or processing in progress. Please try again later.'}, status=202)
        return Response(file_instance.parsed_content or {})
