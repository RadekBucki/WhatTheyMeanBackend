from datetime import datetime
from typing import Iterator

import dotenv
from bson import binary, ObjectId
from mongodb_odm import connect

from backend.exceptions.document_not_found_exception import DocumentNotFoundException
from backend.model.analysis import Analysis


class DataBaseService:
    connect(dotenv.dotenv_values().get("MONGO_DB_URI"))

    @staticmethod
    def create_analysis(raw_file: binary.Binary = None, link: str = None) -> ObjectId:
        return Analysis(raw_file=raw_file, link=link).create().id

    @staticmethod
    def get_analysis_by_uuid(uuid: ObjectId) -> Analysis:
        analysis = Analysis.find_one({"_id": uuid})
        if analysis:
            return analysis
        else:
            raise DocumentNotFoundException("Analysis with id " + str(uuid) + " not found in collection")

    @staticmethod
    def get_analyses_by_uuids(id_list: list[ObjectId]) -> Iterator[Analysis]:
        return Analysis.find(filter={"_id": {"$in": id_list}})

    @staticmethod
    def update_analysis_by_id(uuid: str, **kwargs):
        analysis = DataBaseService.get_analysis_by_uuid(uuid=ObjectId(uuid))

        for key, value in kwargs.items():
            if value is not None:
                setattr(analysis, key, value)

        analysis.finish_date = datetime.now() if 'finish_date' not in kwargs else analysis.finish_date

        analysis.update()
