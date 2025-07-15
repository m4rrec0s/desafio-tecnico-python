# JSONPlaceholder API Consumer

A simple FastAPI backend that consumes the JSONPlaceholder public API to retrieve posts.

## Features

- **GET /** - Root endpoint with welcome message
- **GET /posts/{id}** - Retrieve a specific post by ID from JSONPlaceholder API
- Asynchronous HTTP requests using `httpx`
- Proper error handling with 404 responses for non-existent posts
- Built with FastAPI for automatic API documentation

## Requirements

- Python 3.8+
- FastAPI
- httpx
- uvicorn

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd desafio-tecnico-python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Using Python directly:
```bash
python main.py
```

### Using uvicorn:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application will start on `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- **Interactive API documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative documentation (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### GET /

Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the JSONPlaceholder API Consumer!"
}
```

### GET /posts/{id}

Retrieves a post by ID from the JSONPlaceholder API.

**Parameters:**
- `id` (int): The post ID to retrieve

**Response (Success):**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit..."
}
```

**Response (Error - 404):**
```json
{
  "detail": "Post not found"
}
```

## Examples

### Get welcome message:
```bash
curl http://localhost:8000/
```

### Get post by ID:
```bash
curl http://localhost:8000/posts/1
```

### Test non-existent post:
```bash
curl http://localhost:8000/posts/999
```

## Development

The application is structured as a single file (`main.py`) for simplicity, containing:

- FastAPI application instance
- Root endpoint handler
- Post retrieval endpoint with error handling
- Asynchronous HTTP client using httpx

## Error Handling

- **404 Not Found**: When a post doesn't exist in JSONPlaceholder
- **500 Internal Server Error**: For network or other HTTP errors

## External API

This application consumes the JSONPlaceholder API:
- Base URL: https://jsonplaceholder.typicode.com
- Endpoint used: `/posts/{id}`