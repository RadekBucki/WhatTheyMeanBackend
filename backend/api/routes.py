from flask import Blueprint, render_template

from backend.model.status import Status

api = Blueprint('api', __name__)

@api.route('/register/file', methods=['POST'])
def register_file():
    return "Register file"

@api.route('/register/url', methods=['POST'])
def register_url():
    return "Register url"

@api.route('/analyse/<analyse_id>', methods=['GET'])
def get_analyse(analyse_id: int):
    return f"Get analyse {analyse_id} with status {Status.QUEUED}"

@api.route('/analyse', methods=['GET'])
def get_analyses():
    return "Get list of analyses"

# for testing purposes
@api.route('/', methods=['GET'])
def for_test():
    return render_template('index.html')