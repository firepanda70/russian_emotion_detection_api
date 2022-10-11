from fastapi import APIRouter, Body

from schemas import Emotion, RussianEmotionDetectedList, RussianEmotionPost
from predictor import predict_emotions


router = APIRouter()


@router.post(
    '/russian_emotion_post',
    response_model=RussianEmotionDetectedList,
    tags=['API Methods']
)
async def detect_emotion(
    emotion_model: RussianEmotionPost = Body(
        examples={
            'enthusiasm': {
                'summary': 'Пример эмоции энтузиазм',
                'description': ('Будет возвращен список с '
                                'приорететной эмоцией энтузиазм'),
                'value': {
                    'text': 'Как дела?'
                },
            },
            'anger': {
                'summary': 'Пример эмоции злости',
                'description': 'Вы обидели деда',
                'value': {
                    'text': 'Дурак твой дед'
                },
            },
            'sadness': {
                'summary': 'Пример эмоции под названием грустно',
                'description': 'А я не хочу на работу',
                'value': {
                    'text': 'Не хочу в школу('
                },
            },
        },
    ),
):
    """
    Возвращает список предсказанных эмоций и их
    вероятностей в тексте на русском языке.
    """
    emotions = predict_emotions(emotion_model.text)
    results = [Emotion(label=key, score=value)
               for key, value in emotions.items()]
    return RussianEmotionDetectedList(results=results)
