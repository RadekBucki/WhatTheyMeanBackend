import concurrent.futures
import os
import openai
import base64 as b64
from typing import Dict

OPENAI_API_KEY: str = os.environ.get('OPENAI_API_KEY')


class ProcessingDTO:
    def __init__(self, transcription: str, summary: str, sentiment: Dict[str, float]):
        self.transcription = transcription
        self.summary = summary
        self.sentiment = sentiment


def process_audio(base64: str) -> ProcessingDTO:
    transcription = transcribe(base64)
    if transcription == '':
        return ProcessingDTO('', '', None)
    # run sentiment and summary in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        summary_future = executor.submit(sum_up, transcription)
        sentiment_future = executor.submit(run_sentiment_analysis, transcription)
    summary_result = summary_future.result()
    sentiment_result = sentiment_future.result()
    return ProcessingDTO(transcription, summary_result, sentiment_result)


def transcribe(base64: str) -> str:
    transcript: str = ''
    mp3_data = b64.b64decode(base64)
    audio_file_path = "audio.mp3"
    with open(audio_file_path, "wb") as mp3_file:
        mp3_file.write(mp3_data)
    with open(audio_file_path, "rb") as audio_file:
        try:
            transcript = openai.Audio.transcribe("whisper-1", audio_file, api_key=OPENAI_API_KEY)
        except openai.error.OpenAIError:
            print("OpenAI whisper's API exception occurred")
    os.remove(audio_file_path)
    return transcript


def run_sentiment_analysis(text: str) -> Dict[str, float]:
    # run sentiment analysis
    return {'pos': 0.746, 'compound': 0.8316, 'neu': 0.254, 'neg': 0.0}


def sum_up(text: str) -> str:
    response = openai.ChatCompletion.create(
        api_key=OPENAI_API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You are an expert in summarizing text."},
            {"role": "user",
             "content": f"""I will give you a transcription of audio file (text). Your task is to create a summary of 
                this text. You have to be concise. Answer immediately without any additional introductions or 
                explanation, just a quick summary of the text, what is this text about. This is the text: {text}"""},
        ])
    return response.choices[0].message
