from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from code.config import load_config
from code.utils.logger import logger
import os

config = load_config()

app = Flask(__name__)
CORS(app, origins=config["allowed_origins"])

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per day", "20 per hour", "5 per minute"]
)

@app.route('/health', methods=['GET'])
@limiter.limit("1000 per minute")
def health_check():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    logger.info(f"Starting Email Service API on port {port}, Debug mode: {debug}")
    app.run(host='0.0.0.0', port=port, debug=debug)