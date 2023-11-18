import os
import unittest

from pytube.exceptions import VideoUnavailable

from backend.video_parser.YouTubeDownloader import YouTubeDownloader


class TestSentimentAnalysis(unittest.TestCase):

    def test_import_from_youtube_positive(self):
        res = YouTubeDownloader.download("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertIsNotNone(res)
        f = open("test_video_parser_res.txt", "r")
        self.assertEqual(res, f.read())
        self.assertFalse(os.path.isfile("audio.mp3"))
        self.assertFalse(os.path.isfile("audio.mp4"))

    def test_import_from_youtube_negative_link_not_exist(self):
        with self.assertRaises(VideoUnavailable):
            YouTubeDownloader.download("https://www.youtube.com/watch?v=duafasfsafkjasbfkasfksafas")
        self.assertFalse(os.path.isfile("audio.mp3"))
        self.assertFalse(os.path.isfile("audio.mp4"))


if __name__ == '__main__':
    unittest.main()