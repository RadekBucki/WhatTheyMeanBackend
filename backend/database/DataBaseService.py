import pymongo
from Analysis import Analysis
import dotenv
import time
import dotenv
from datetime import datetime


class DataBaseService:

    def __init__(self):
        root_name = dotenv.dotenv_values().get('MONGO_INITDB_ROOT_USERNAME')
        root_password = dotenv.dotenv_values().get('MONGO_INITDB_ROOT_PASSWORD')
        CONNECTION_STRING = 'mongodb://' + root_name + ':' + root_password + '@localhost:27017/admin?authSource=admin'
        self.db_client = pymongo.MongoClient(CONNECTION_STRING)
        #   Hardcoded database and collection names
        self.db = self.db_client["whatTheyMeanDB"]
        self.collection = self.db["analyses"]

    def create_analysis(self, file=None, link=None):
        latest_record = self.collection.find_one(sort=[("_id", pymongo.DESCENDING)])
        if latest_record:
            uuid = str(int(latest_record.get("uuid")) + 1)
        else:
            uuid = '1'

        date_time = datetime.fromtimestamp(int(time.time()))
        formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

        analysis = Analysis(
            uuid=uuid,
            # name=,
            start_date=formatted_date_time,
            # end_date=,
            # status=,
            file_type=None,
            link=link,
            raw_file=file,
            # full_transcription=,
            # video_summary=,
            # author_attitude=
        )
        self.collection.insert_one(analysis.to_dict())
        return uuid

    def get_analysis_by_id(self, uuid):
        return Analysis.from_dict(self.collection.find_one({"uuid": uuid}))

    def get_all_analyses(self):
        analyses = []
        for document in self.collection.find():
            analyses.append(Analysis.from_dict(document))
        return analyses

    def update_analysis_by_id(self, uuid, status, full_transcription, video_summary, author_attitude):
        date_time = datetime.fromtimestamp(int(time.time()))
        formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

        query = {"uuid": uuid}
        update_data = {
            "$set": {
                "end_date": formatted_date_time,
                "status": status,
                "full_transcription": full_transcription,
                "video_summary": video_summary,
                "author_attitude": author_attitude
            }
        }
        self.collection.update_one(query, update_data)
