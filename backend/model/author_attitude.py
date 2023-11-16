from enum import Enum


class AuthorAttitude(str, Enum):
    POSITIVE = "pos"
    NEGATIVE = "neg"
    NEUTRAL = "neu"
    COMPOUND = "compound"
