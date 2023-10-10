import os
from typing import Dict

OPENAI_API_KEY: str = os.environ.get('OPENAI_API_KEY')


class ProcessingDTO:
    def __init__(self, transcription: str, summary: str, sentiment: Dict[str, float]):
        self.transcription = transcription
        self.summary = summary
        self.sentiment = sentiment


def process_audio(base64: str) -> ProcessingDTO:
    transcription = transcribe(base64)
    summary_result = sum_up(transcription)
    sentiment_result = run_sentiment_analysis(transcription)
    return ProcessingDTO(transcription, summary_result, sentiment_result)


def transcribe(base64: str) -> str:
    # transcribe audion in parallel
    return "lorem ipsum"


def run_sentiment_analysis(text: str) -> Dict[str, float]:
    # run sentiment analysis
    return {'pos': 0.746, 'compound': 0.8316, 'neu': 0.254, 'neg': 0.0}


def sum_up(text: str) -> str:
    return "shortened text"
