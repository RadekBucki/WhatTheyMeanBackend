import logging

from flask import jsonify

logger = logging.getLogger(__name__)

def handle_500_error(e):
    logger.error(e)
    return jsonify({'error': str(e)}), 500

def handle_bad_request(e):
    logger.warning(e)
    return jsonify({'error': str(e)}), 400