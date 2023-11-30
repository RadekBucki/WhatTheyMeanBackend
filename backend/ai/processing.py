import concurrent.futures
import os

from openai import OpenAI
import base64 as b64
from typing import Dict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()


class Processing:
    def __init__(self, transcription: str, summary: str, sentiment: Dict[str, float]):
        self.transcription = transcription
        self.summary = summary
        self.sentiment = sentiment


def process_audio(base64) -> Processing:
    transcription = transcribe(base64)
    if transcription == '':
        return Processing('', '', None)
    # run sentiment and summary in parallel
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     summary_future = executor.submit(sum_up, transcription)
    #     sentiment_future = executor.submit(run_sentiment_analysis, transcription)
    # summary_result = summary_future.result()
    # sentiment_result = sentiment_future.result()
    return Processing(transcription, sum_up(transcription), run_sentiment_analysis(transcription))


def transcribe(base64) -> str:
    key = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key=key)
    mp3_data = b64.b64decode(base64)
    audio_file_path = "audio.mp3"
    with open(audio_file_path, "wb") as mp3_file:
        mp3_file.write(mp3_data)
    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file).text
    os.remove(audio_file_path)
    return transcript


def run_sentiment_analysis(text: str) -> Dict[str, float]:
    return sentiment_analyzer.polarity_scores(text)


def sum_up(text: str) -> str:
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in summarizing text."},
            {"role": "user", "content": f"""You will receive a transcription of an audio file (text). Your task is to create a summary of 
                this text. You have to be concise and use english no matter what the original language is.
                Answer immediately without any additional introductions or explanation, just a summary. 
                This is the input: {text}"""}
        ]
    )
    return response.choices[0].message.content
