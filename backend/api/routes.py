from flask import Blueprint, render_template

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def for_test():
    return render_template('index.html')

@api.route('/analyse/<analyse_id>', methods=['GET'])
def get_analyse(analyse_id: int):
    return f"Get analyse {analyse_id}"