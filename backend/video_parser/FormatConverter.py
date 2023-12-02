import base64

from moviepy.video.io.VideoFileClip import VideoFileClip


class FormatConverter:

    @staticmethod
    def get_video_path() -> str:
        return "audio.mp4"

    @staticmethod
    def get_audio_path() -> str:
        return "audio.mp3"

    @staticmethod
    def convert() -> str:
        video_file_path = FormatConverter.get_video_path()
        audio_file_path = FormatConverter.get_audio_path()
        video = VideoFileClip(video_file_path)
        video.audio.write_audiofile(audio_file_path)
        video.close()
        with open(audio_file_path, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode()
        return audio_base64
