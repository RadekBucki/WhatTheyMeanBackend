import base64
import os

from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube


class YouTubeDownloader:

    @staticmethod
    def download(url: str) -> str:
        video_file_path = "audio.mp4"
        audio_stream = YouTube(url).streams.filter(file_extension='mp4').first()
        audio_stream.download(output_path='', filename=video_file_path)
        video = VideoFileClip(video_file_path)
        audio_file_path = "audio.mp3"
        video.audio.write_audiofile(audio_file_path)
        video.close()
        with open(audio_file_path, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode()
        os.remove(video_file_path)
        os.remove(audio_file_path)
        return audio_base64
