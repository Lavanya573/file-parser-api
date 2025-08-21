from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'id', 'name', 'file', 'status', 'progress', 'parsed_content', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'status', 'progress', 'parsed_content', 'created_at', 'updated_at'] 