from typing import List

from pydantic import BaseModel, Field


class Emotion(BaseModel):
    label: str
    score: float


class RussianEmotionPost(BaseModel):
    text: str = Field(..., min_length=1)


class RussianEmotionDetectedList(BaseModel):
    results: List[Emotion]
