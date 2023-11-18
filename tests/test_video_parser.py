import os
import unittest

from pytube.exceptions import VideoUnavailable

from backend.video_parser.YouTubeDownloader import YouTubeDownloader

AUDIO_FILE_PATH = "audio.mp3"
VIDEO_FILE_PATH = "audio.mp4"


class TestSentimentAnalysis(unittest.TestCase):

    def test_import_from_youtube_positive(self):
        res = YouTubeDownloader.download("https://www.youtube.com/watch?v=Uv4tHSINZn0")
        self.assertIsNotNone(res)
        f = open("tests/resources/test_video_parser_res.txt", "r")
        self.assertEqual(len(res), len(f.read()))
        self.assertFalse(os.path.isfile(AUDIO_FILE_PATH))
        self.assertFalse(os.path.isfile(VIDEO_FILE_PATH))

    def test_import_from_youtube_negative_link_not_exist(self):
        with self.assertRaises(VideoUnavailable):
            YouTubeDownloader.download("https://www.youtube.com/watch?v=duafasfsafkjasbfkasfksafas")
        self.assertFalse(os.path.isfile(AUDIO_FILE_PATH))
        self.assertFalse(os.path.isfile(VIDEO_FILE_PATH))


if __name__ == '__main__':
    unittest.main()