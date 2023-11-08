from bson import ObjectId
from datetime import datetime

from backend.app import db
from backend.model.analysis import Analysis
from backend.model.dict_dataclass_converters import *


class DataBaseService:

    @staticmethod
    def create_analysis(file=None, link=None):
        return db.analyses.insert_one(dataclass_to_dict(Analysis(link=link, raw_file=file))).inserted_id

    @staticmethod
    def get_analysis_by_id(uuid):
        dict = db.analyses.find_one({"_id": ObjectId(str(uuid))})
        if dict:
            return dict_to_dataclass(dict, Analysis)
        else:
            return None

    @staticmethod
    def get_all_analyses():
        dataclass_analyses = []
        for dict_analysis in db.analyses.find():
            dataclass_analyses.append(dict_to_dataclass(dict_analysis, Analysis))
        return dataclass_analyses

    @staticmethod
    def update_analysis_by_id(uuid, status, full_transcription, video_summary, author_attitude, raw_file=None):
        db.analyses.update_one({"_id": ObjectId(str(uuid))}, {
            "$set": {
                "finish_date": datetime.now(),
                "status": status.value,
                "raw_file": raw_file,
                "full_transcription": full_transcription,
                "video_summary": video_summary,
                "author_attitude": author_attitude.value
            }
        })

