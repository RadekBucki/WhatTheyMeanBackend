import os
from typing import Dict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

OPENAI_API_KEY: str = os.environ.get('OPENAI_API_KEY')

sentiment_analyzer = SentimentIntensityAnalyzer()


class Processing:

    def __init__(self):
        pass


def transcribe(base64: str) -> str:
    # transcribe audion in parallel
    return "lorem ipsum"


def run_sentiment_analysis(text: str) -> Dict[str, float]:
    return sentiment_analyzer.polarity_scores(text)


def sum_up(text: str) -> str:
    return "shortened text"
