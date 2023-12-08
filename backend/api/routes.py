import logging
from typing import Any

from bson import ObjectId
from flask import Blueprint, request, jsonify, Response

from backend.database.database_service import DataBaseService
from backend.exceptions.illegal_argument_exception import IllegalArgumentException

api = Blueprint('api', __name__)
logger = logging.getLogger(__name__)


@api.route('/register/file', methods=['POST'])
def register_file() -> Response:
    if 'file' not in request.files:
        raise IllegalArgumentException('No file part')

    file = request.files.get('file')
    logger.info(f"Received file: {file}")
    result: ObjectId = DataBaseService.create_analysis(raw_file=file.read())

    return jsonify({'analysis_uuid': str(result)})


@api.route('/register/url', methods=['POST'])
def register_url() -> Response:
    url = request.args.get('url')

    if not url:
        raise IllegalArgumentException('No url part')
    logger.info(f"Received url: {url}")
    result: ObjectId = DataBaseService.create_analysis(link=url)

    return jsonify({'analysis_uuid': str(result)})


@api.route('/analyse/<analyse_uuid>', methods=['GET'])
def get_analyse(analyse_uuid: str) -> Response:
    analysis = DataBaseService.get_analysis_by_uuid(ObjectId(analyse_uuid)).to_mongo()
    if 'raw_file' in analysis:
        del analysis['raw_file']
    logger.debug(f"Received analysis: {analysis}")
    return jsonify(analysis)


@api.route('/analyse', methods=['GET'])
def get_analyses() -> list[dict[str, Any]]:
    uuid_list = request.args.get('uuids').split(',')

    if not uuid_list:
        raise IllegalArgumentException('No uuids part')
    logger.info(f"Received uuids: {uuid_list}")
    object_id_list = [ObjectId(uuid) for uuid in uuid_list]
    object_list = [analysis.to_mongo() for analysis in DataBaseService.get_analyses_by_uuids(object_id_list)]
    for analysis in object_list:
        if 'raw_file' in analysis:
            del analysis['raw_file']

    return object_list
