# File Parser CRUD API with Progress Tracking

A Django REST Framework backend application that supports uploading, storing, parsing, and retrieving files with real-time progress tracking for large uploads.

## Features

- **File Upload API** - POST files with multipart form-data
- **Progress Tracking** - Real-time progress updates during processing
- **Background Parsing** - Asynchronous file processing with threading
- **CSV Support** - Automatic CSV parsing with structured output
- **CRUD Operations** - Full Create, Read, Update, Delete functionality
- **Status Management** - Track upload/processing/ready/failed states

## Tech Stack

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: SQLite (configurable for production)
- **File Storage**: Django's built-in file storage
- **Parsing**: Python csv module for CSV files
- **Progress**: Background threading with database updates

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd file_parser
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install "Django>=4.2,<5" djangorestframework openpyxl
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### 1. File Upload
**POST** `/files/`

Upload a file for processing.

**Request:**
```bash
curl -X POST -F "name=My File" -F "file=@data.csv" http://127.0.0.1:8000/files/
```

**Response:**
```json
{
  "id": "03057cd4-33b4-4714-9fde-ecd1a4b8092b",
  "name": "My File",
  "file": "http://127.0.0.1:8000/media/uploads/data.csv",
  "status": "uploading",
  "progress": 1,
  "parsed_content": null,
  "created_at": "2025-08-20T17:35:25.333682Z",
  "updated_at": "2025-08-20T17:35:25.333682Z"
}
```

### 2. Progress Tracking
**GET** `/files/{file_id}/progress/`

Check the current processing status and progress.

**Request:**
```bash
curl http://127.0.0.1:8000/files/03057cd4-33b4-4714-9fde-ecd1a4b8092b/progress/
```

**Response:**
```json
{
  "file_id": "03057cd4-33b4-4714-9fde-ecd1a4b8092b",
  "status": "processing",
  "progress": 45
}
```

**Status Values:**
- `uploading` - File is being uploaded
- `processing` - File is being parsed/processed
- `ready` - Processing complete, content available
- `failed` - Processing failed

### 3. Get File Content
**GET** `/files/{file_id}/`

Retrieve parsed content when processing is complete.

**Request:**
```bash
curl http://127.0.0.1:8000/files/03057cd4-33b4-4714-9fde-ecd1a4b8092b/
```

**Response (Ready):**
```json
[
  {"name": "Alice", "age": "30"},
  {"name": "Bob", "age": "25"}
]
```

**Response (Still Processing):**
```json
{
  "message": "File upload or processing in progress. Please try again later."
}
```

### 4. List Files
**GET** `/files/`

List all uploaded files with metadata.

**Request:**
```bash
curl http://127.0.0.1:8000/files/
```

**Response:**
```json
[
  {
    "id": "03057cd4-33b4-4714-9fde-ecd1a4b8092b",
    "name": "Test CSV 2",
    "file": "http://127.0.0.1:8000/media/uploads/sample.csv",
    "status": "ready",
    "progress": 100,
    "parsed_content": [...],
    "created_at": "2025-08-20T17:35:25.333682Z",
    "updated_at": "2025-08-20T17:35:25.333682Z"
  }
]
```

### 5. Delete File
**DELETE** `/files/{file_id}/`

Remove a file and its parsed content.

**Request:**
```bash
curl -X DELETE http://127.0.0.1:8000/files/03057cd4-33b4-4714-9fde-ecd1a4b8092b/
```

**Response:** HTTP 204 No Content

## File Processing

### Supported Formats
- **CSV Files**: Automatically parsed using Python's csv module
- **Other Files**: Simulated processing with progress updates

### Processing Flow
1. File upload triggers background processing thread
2. Status changes from `uploading` → `processing` → `ready`
3. Progress updates from 1% → 100%
4. Parsed content stored in JSON format
5. File available for retrieval

## Database Schema

```python
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    progress = models.IntegerField(default=0)
    parsed_content = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## Testing the API

### 1. Create Sample CSV
```bash
echo "name,age" > sample.csv
echo "Alice,30" >> sample.csv
echo "Bob,25" >> sample.csv
```

### 2. Upload File
```bash
curl -X POST -F "name=Test CSV" -F "file=@sample.csv" http://127.0.0.1:8000/files/
```

### 3. Monitor Progress
```bash
# Replace {file_id} with actual ID from upload response
curl http://127.0.0.1:8000/files/{file_id}/progress/
```

### 4. Fetch Content
```bash
curl http://127.0.0.1:8000/files/{file_id}/
```

## Production Considerations

- **Database**: Use PostgreSQL or MySQL for production
- **File Storage**: Configure cloud storage (AWS S3, Azure Blob)
- **Background Tasks**: Replace threading with Celery or RQ
- **Authentication**: Add JWT or session-based auth
- **Rate Limiting**: Implement API rate limiting
- **Monitoring**: Add logging and metrics collection

## Development

- **Server**: `python manage.py runserver`
- **Migrations**: `python manage.py makemigrations && python manage.py migrate`
- **Admin**: `python manage.py createsuperuser` then visit `/admin/`

## License

This project is open source and available under the MIT License. 