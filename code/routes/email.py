from flask import Blueprint, request, jsonify
from code.email_sender import send_email_background
from code.config import load_config
from code.utils.logger import logger
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
config = load_config()
email_bp = Blueprint('email', __name__)
executor = ThreadPoolExecutor(max_workers=5)

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key and api_key == config['api_key']:
            return f(*args, **kwargs)
        else:
            logger.warning(f"Unauthorized access attempt from {request.remote_addr}")
            return jsonify({"error": "Unauthorized access"}), 401
    return decorated_function

@email_bp.route('/api/send-email', methods=['POST'])
@require_api_key
def email_handler():
    try:
        data = request.json
        if not data or 'subject' not in data or 'message' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        executor.submit(send_email_background,data)
        return jsonify({"status": "success", "message": "Request submitted successfully."}), 200

    except Exception as e:
        logger.exception(f"Error in email handler: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@email_bp.route('/api/reload-config', methods=['POST'])
@require_api_key
def reload_config():
    global config
    config = load_config()
    return jsonify({"status": "success", "message": "Configuration reloaded"}), 200

