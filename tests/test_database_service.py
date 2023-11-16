import datetime
import unittest

from bson import ObjectId

from backend.database.database_service import DataBaseService
from backend.exceptions.document_not_found_exception import DocumentNotFoundException
from backend.model.analysis import Analysis
from backend.model.author_attitude import AuthorAttitude
from backend.model.status import Status


class TestDatabaseService(unittest.TestCase):

    def test_create_and_get_analysis(self):
        analysis_id = DataBaseService.create_analysis(link="link_to_video")
        date = datetime.datetime.now()
        created_analysis = DataBaseService.get_analysis_by_uuid(analysis_id)

        self.assertEqual(created_analysis.id, analysis_id)
        self.assertEqual(created_analysis.name, "Analysis")
        self.assertEqual(created_analysis.start_date.date(), date.date())
        self.assertIsNone(created_analysis.finish_date)
        self.assertEqual(created_analysis.status, Status.IN_PROGRESS)
        self.assertIsNone(created_analysis.file_type)
        self.assertEqual(created_analysis.link, "link_to_video")
        self.assertIsNone(created_analysis.raw_file)
        self.assertIsNone(created_analysis.full_transcription)
        self.assertIsNone(created_analysis.video_summary)
        self.assertIsNone(created_analysis.author_attitude)

        Analysis().delete_one({"_id": analysis_id})

    def test_get_non_existent_analysis(self):
        self.assertRaises(DocumentNotFoundException, DataBaseService.get_analysis_by_uuid,
                          ObjectId("111122223333444455556666"))

    def test_get_multiple_analyses(self):
        analysis_ids = []
        searched_ids = []
        for i in range(3):
            analysis_id = DataBaseService.create_analysis(link="link_to_video_" + str(i))
            analysis_ids.append(analysis_id)
        searched_ids.append(analysis_ids[0])
        searched_ids.append(analysis_ids[2])

        analyses = DataBaseService.get_analyses_by_uuids(searched_ids)
        for i, analysis in enumerate(analyses):
            self.assertEqual(analysis.id, searched_ids[i])

        for analysis_id in analysis_ids:
            Analysis().delete_one({"_id": analysis_id})

    def test_update_analysis(self):
        analysis_id = DataBaseService.create_analysis(link="link_to_video")
        DataBaseService.update_analysis_by_id(uuid=analysis_id, status=Status.SUCCESS,
                                              full_transcription="full_transcription",
                                              video_summary="video_summary", author_attitude=AuthorAttitude.POSITIVE)
        date = datetime.datetime.now()
        updated_analysis = DataBaseService.get_analysis_by_uuid(analysis_id)
        self.assertEqual(updated_analysis.id, analysis_id)
        self.assertEqual(updated_analysis.finish_date.date(), date.date())
        self.assertEqual(updated_analysis.status, Status.SUCCESS)
        self.assertEqual(updated_analysis.full_transcription, "full_transcription")
        self.assertEqual(updated_analysis.video_summary, "video_summary")
        self.assertEqual(updated_analysis.author_attitude, AuthorAttitude.POSITIVE)

        Analysis().delete_one({"_id": analysis_id})


if __name__ == '__main__':
    unittest.main()
