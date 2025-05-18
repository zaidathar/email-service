from flask import Flask
from flask_cors import CORS
from code.config import load_config
from code.utils.logger import logger
import os

config = load_config()

app = Flask(__name__)
CORS(app, origins=config["allowed_origins"])


@app.route('/health', methods=['GET'])
def health_check():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    logger.info(f"Starting Email Service API on port {port}, Debug mode: {debug}")
    app.run(host='0.0.0.0', port=port, debug=debug)