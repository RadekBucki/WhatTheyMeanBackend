import os
import unittest

from pytube.exceptions import VideoUnavailable

from backend.video_parser.FormatConverter import FormatConverter
from backend.video_parser.TikTokDownloader import TikTokDownloader
from backend.video_parser.YouTubeDownloader import YouTubeDownloader


class TestVideoParser(unittest.TestCase):

    def test_import_from_youtube_positive(self):
        res = YouTubeDownloader.download("https://www.youtube.com/watch?v=Uv4tHSINZn0")
        self.assertIsNotNone(res)
        f = open("tests/resources/test_video_parser_res.txt", "r")
        self.assertEqual(len(res), len(f.read()))
        self.assertFalse(os.path.isfile(FormatConverter.get_audio_path()))
        self.assertFalse(os.path.isfile(FormatConverter.get_video_path()))

    def test_import_from_youtube_negative_link_not_exist(self):
        with self.assertRaises(VideoUnavailable):
            YouTubeDownloader.download("https://www.youtube.com/watch?v=duafasfsafkjasbfkasfksafas")
        self.assertFalse(os.path.isfile(FormatConverter.get_audio_path()))
        self.assertFalse(os.path.isfile(FormatConverter.get_video_path()))

    def test_import_from_tiktok_positive(self):
        res = TikTokDownloader.download("https://www.tiktok.com/@tiktok/video/7106594312292453675?is_copy_url=1&is_from_webapp=v1")
        self.assertIsNotNone(res)
        f = open("tests/resources/test_video_parser_res2.txt", "r")
        self.assertEqual(len(res), len(f.read()))
        self.assertFalse(os.path.isfile(FormatConverter.get_audio_path()))
        self.assertFalse(os.path.isfile(FormatConverter.get_video_path()))

    def test_import_from_tiktok_negative_link_not_exist(self):
        with self.assertRaises(KeyError):
            TikTokDownloader.download("https://www.tiktok.com/@tiktok/video/710gasgsg53675?is_copy_url=1&is_from_webapp=v1")
        self.assertFalse(os.path.isfile(FormatConverter.get_audio_path()))
        self.assertFalse(os.path.isfile(FormatConverter.get_video_path()))


if __name__ == '__main__':
    unittest.main()