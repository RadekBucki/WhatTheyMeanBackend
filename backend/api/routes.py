import logging
from typing import Iterator

from bson import ObjectId
from flask import Blueprint, render_template, request

from backend.database.database_service import DataBaseService
from backend.exceptions.illegal_argument_exception import IllegalArgumentException
from backend.model.analysis import Analysis

api = Blueprint('api', __name__)
logger = logging.getLogger(__name__)

@api.route('/register/file', methods=['POST'])
def register_file() -> ObjectId:
    if 'file' not in request.files:
        raise IllegalArgumentException('No file part')

    file = request.files.get('file')
    logger.info(f"Received file: {file}")

    return DataBaseService.create_analysis(raw_file=file)

@api.route('/register/url', methods=['POST'])
def register_url() -> ObjectId:
    url = request.args.get('url')

    if not url:
        raise IllegalArgumentException('No url part')
    logger.info(f"Received url: {url}")

    return DataBaseService.create_analysis(link=url)

@api.route('/analyse/<analyse_id>', methods=['GET'])
def get_analyse(analyse_id: ObjectId) -> Analysis:
    return DataBaseService.get_analysis_by_id(analyse_id)

@api.route('/analyse', methods=['GET'])
def get_analyses(id_list: list[ObjectId]) -> Iterator[Analysis]:
    return DataBaseService.get_analyses_by_ids(id_list)

# for socket connection testing purposes
@api.route('/', methods=['GET'])
def for_test():
    return render_template('index.html')