# FastAPI Backend

This is an application that uses FastAPI to create a simple backend server. The server returns a list of numbers and a contact name.

## Endpoints

- **GET /**: Returns a list of numbers.
- **GET /contact**: Returns the contact name.

## Requirements

- Python 3.8 or higher
- `fastapi` library
- `uvicorn` library

## Setup & Run
```bash
# Configure virtual environment
pyenv install 3.12
pyenv virtualenv 3.12.17 fastapi
pyenv activate fastapi

# Install dependencies and run the application
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload

# Open the browser and navigate to http://127.0.0.1:8000

```

Notes: started this project with these libraries:
```bash
pip install fastapi
pip3 install "uvicorn[standard]"
pip3 freeze > requirements.txt
```

## Docker build and run
```bash
# Build and run the application
docker-compose build
docker-compose up -d

# Open the browser and navigate to http://127.0.0.1:8000

# Stop the application
docker-compose down

# Check inside the container
docker-compose exec fastapi bash

```