
import os
from dotenv import load_dotenv
from code.utils.logger import logger

load_dotenv()

def load_config():
    smtp_port = os.getenv("SMTP_PORT")
    if smtp_port is None:
        raise ValueError("SMTP_PORT is not defined in the environment")

    return {
        "receivers": os.getenv("DEFAULT_EMAIL_RECEIVERS", os.getenv("DEFAULT_EMAIL_RECEIVER", "")).split(','),
        "smtp": {
            "server": os.getenv("SMTP_SERVER", "smtp.titan.email"),
            "port": int(smtp_port),
            "username": os.getenv("SMTP_USERNAME", ""),
            "password": os.getenv("SMTP_PASSWORD", "")
        },
        "api_key": os.getenv("API_KEY", "your-secret-api-key"),
        "allowed_origins": os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(',')
    }
