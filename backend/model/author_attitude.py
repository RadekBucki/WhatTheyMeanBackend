from enum import Enum


class AuthorAttitude(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    COMPOUND = "compound"
