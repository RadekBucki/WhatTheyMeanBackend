import base64
import os
from pytube import YouTube


class YouTubeDownloader:

    @staticmethod
    def download(url: str) -> str:
        audio_file_path = "audio.mp4"
        audio_stream = YouTube(url).streams.filter(only_audio=True, file_extension='mp3').first()
        audio_stream.download(output_path='', filename=audio_file_path)
        with open(audio_file_path, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode()
        os.remove(audio_file_path)
        return audio_base64
