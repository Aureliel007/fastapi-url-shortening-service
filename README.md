# FastAPI URL Shortening Service

This service provides an API for shortening URLs using FastAPI and is containerized using Docker.

## Getting Started

### 1. Prerequisites

- Ubuntu 22.04, 24.04, or the latest non-LTS version
- [Docker](https://docs.docker.com/desktop/setup/install/linux/ubuntu/) installed on your machine.

### 2. Clone the Repository

```
git clone https://github.com/Aureliel007/fastapi-url-shortening-service.git
cd fastapi-url-shortening-service
```

## Setup

### 1. Environment Variables

Create a .env file in the project root directory with the following content:
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=
```

### 2. Building and Running with Docker

Start the service with docker-compose:
```
docker-compose up
```

## API Documentation

Once the service is running, interactive API documentation is available 
at Swagger UI: http://<your-address>:8080/docs

### Main Endpoints

1. Shorten URL

   - Endpoint: POST /shorten

   - Description: Creates a shortened URL.

   - Request Body:

        ```json
        {
        "url": "https://example.com"
        }
        ```
    - Response provides short URL ID:
        ```json
        {
        "short_url": "abcd1234"
        }
        ```

2. Redirect to Original URL

   - Endpoint: GET /{short_code}

   - Description: Redirects to the original URL based on the provided short code.

   - Example Request: GET /abcd1234
  