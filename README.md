
# Email Service API

A simple email service built with Flask that supports background email sending and secure API key access.

## Features
- Background email sending using ThreadPool
- Uses SMTP server to send email.
- CORS and API key security
- Environment-based config with `.env`
- Dockerized
- Poetry for dependency management

## Usage

- Clone the repository 

### Run locally 
1. Create virtual environment 
```bash
cd email-service
python3 -m venv venv # Create virtual environment
source ./venv/bin/activate # Active virtual environment

```
2. Install `poetry ` using `pip install poetry`
3. Install all dependency using poetry
```bash
poetry install
```

```bash
docker build -t email-service .
docker run --env-file .env -p 5000:5000 email-service
```

## Endpoints
- `POST /api/send-email`
- `GET /health`
- `POST /api/reload-config`

## .env file
```bash
SMTP_PORT=587
SMTP_SERVER=<SMTP Server Provider>
SMTP_USERNAME=<Email-Address>
SMTP_PASSWORD=<Password>
API_KEY=<your-secret-api-key>
DEFAULT_EMAIL_RECEIVER=<Default-email>
DEBUG=False
ALLOWED_ORIGINS=<Allowed Origin to access service>
```