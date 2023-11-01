import logging

from flask import Blueprint, render_template, request

api = Blueprint('api', __name__)
logger = logging.getLogger(__name__)

@api.route('/register/file', methods=['POST'])
def register_file():
    if 'file' not in request.files:
        raise Exception('No file part')

    file = request.files.get('file')
    logger.info(f"Received file: {file}")

    return "id and status"

@api.route('/register/url', methods=['POST'])
def register_url():
    url = request.args.get('url')
    if not url:
        raise Exception('No url part')
    logger.info(f"Received url: {url}")
    return "id and status"

@api.route('/analyse/<analyse_id>', methods=['GET'])
def get_analyse(analyse_id: int):
    return f"Get analyse {analyse_id}"

@api.route('/analyse', methods=['GET'])
def get_analyses():
    return []

# for socket connection testing purposes
@api.route('/', methods=['GET'])
def for_test():
    return render_template('index.html')