
# Email Service API

---

## Overview

The **Simple Email Service API** is a lightweight and robust Flask application designed to handle email sending efficiently and securely. It provides a dedicated RESTful endpoint for sending emails, offloading the actual SMTP communication to a background thread pool. This ensures that your API remains responsive, even during high email volumes or slow SMTP server responses.

Built with security in mind, the service incorporates API key authentication and CORS protection, making it suitable for integration into various applications. Its Dockerized setup and Poetry-managed dependencies ensure a consistent and portable development and deployment experience.

---

## Features

* **Background Email Sending:** Leverages a `ThreadPoolExecutor` to send emails asynchronously, preventing blocking of the main API thread.
* **SMTP Integration:** Utilizes standard SMTP protocol for reliable email delivery.
* **Secure API Access:**
    * **API Key Authentication:** All API requests require a valid API key for authorization.
    * **CORS (Cross-Origin Resource Sharing) Protection:** Configurable CORS settings to restrict access from unauthorized domains.
* **Environment-based Configuration:** All sensitive and environment-specific settings are managed via `.env` files.
* **Dockerized:** Ready for containerized deployment, ensuring consistency across environments.
* **Poetry for Dependency Management:** Modern and robust dependency management and project packaging.

--- 

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
4. Run app 
    ```bash
    python3 -m code.app
    ```

### Run docker container 
1. Pull Docker image docker repository

    ```bash
        # Pull image from docker repo
        docker pull zaidathar/email-service:0.0.1

        # Run the email service docker container
        docker run --env-file .env -p 5000:5000 zaidathar/email-service:0.0.1

    ```
2. Create your own docker image locally and run container
    ```bash
        # Create docker image from /email-service directory
        docker build -t email-service .

        # Run docker container
        docker run --env-file .env -p 5000:5000 email-service
    ```

---

## Endpoints
- `POST /api/send-email`
- `GET /health`
- `POST /api/reload-config`

---

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
