import dotenv
from datetime import datetime

from mongodb_odm import connect, Document
from typing import Iterator
from bson import binary, ObjectId

from backend.model.analysis import Analysis
from backend.database.exceptions import DocumentNotFoundException
from backend.model.author_attitude import AuthorAttitude
from backend.model.status import Status


class DataBaseService:
    connect(dotenv.dotenv_values().get("MONGO_DB_URI"))

    @staticmethod
    def create_analysis(raw_file: binary.Binary = None, link: str = None) -> ObjectId:
        return Analysis(raw_file=raw_file, link=link).create().id

    @staticmethod
    def get_analysis_by_id(uuid: ObjectId) -> Analysis:
        analysis = Analysis.find_one({"_id": uuid})
        if analysis:
            return analysis
        else:
            raise DocumentNotFoundException("Analysis with id " + str(uuid) + " not found in collection")

    @staticmethod
    def get_analyses_by_ids(id_list: list[ObjectId]) -> Iterator[Analysis]:
        return Analysis.find(filter={"_id": {"$in": id_list}})


    @staticmethod
    def update_analysis_by_id(uuid: ObjectId, status: Status, full_transcription: str, video_summary: str,
                              author_attitude: AuthorAttitude, raw_file: binary.Binary = None):
        analysis = DataBaseService.get_analysis_by_id(uuid=uuid)
        analysis.finish_date = datetime.now()
        analysis.status = status
        analysis.raw_file = raw_file
        analysis.full_transcription = full_transcription
        analysis.video_summary = video_summary
        analysis.author_attitude = author_attitude
        analysis.update()
