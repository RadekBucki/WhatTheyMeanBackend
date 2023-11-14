import dotenv
from datetime import datetime

from mongodb_odm import connect
from backend.model.analysis import Analysis
from backend.database.exceptions import DocumentNotFoundException


class DataBaseService:

    connect(dotenv.dotenv_values().get("MONGO_DB_URI"))

    @staticmethod
    def create_analysis(raw_file=None, link=None):
        return Analysis(raw_file=raw_file, link=link).create().id

    @staticmethod
    def get_analysis_by_id(uuid):
        analysis = Analysis.find_one({"_id": uuid})
        if analysis:
            return analysis
        else:
            raise DocumentNotFoundException("Analysis with _id " + str(uuid) + " not found in collection")

    @staticmethod
    def get_all_analyses():
        return Analysis.find()

    @staticmethod
    def update_analysis_by_id(uuid, status, full_transcription, video_summary, author_attitude, raw_file=None):
        analysis = Analysis.find_one({"_id": uuid})
        if analysis:
            analysis.finish_date = datetime.now()
            analysis.status = status
            analysis.raw_file = raw_file
            analysis.full_transcription = full_transcription
            analysis.video_summary = video_summary
            analysis.author_attitude = author_attitude
            analysis.update()
        else:
            raise DocumentNotFoundException("Analysis with id " + str(uuid) + " not found in collection")
