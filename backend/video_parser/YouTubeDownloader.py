import os

from pytube import YouTube

from backend.video_parser.FormatConverter import FormatConverter


class YouTubeDownloader:

    @staticmethod
    def download(url: str) -> str:
        video_file_path = FormatConverter.get_video_path()
        audio_file_path = FormatConverter.get_audio_path()
        audio_stream = YouTube(url).streams.filter(file_extension='mp4').first()
        audio_stream.download(output_path='', filename=video_file_path)
        audio_base64 = FormatConverter.convert()
        os.remove(video_file_path)
        os.remove(audio_file_path)
        return audio_base64
