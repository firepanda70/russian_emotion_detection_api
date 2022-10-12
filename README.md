# API для модели анализа тональности предожения

## Описание
API со встроенным сервисом [Aniemore](https://github.com/aniemore/Aniemore), который выполняет анализ тональности предложения на русском языке.

## Установка

- Клонировать репозиторий
```
git clone https://github.com/firepanda70/russian_emotion_detection_api
```

- Собрать и запустить Docker контейнер 
```
cd /russian_emotion_detection_api
docker build -t emotion_api .
docker run --name emotion_api -it -p 8000:8000 emotion_api 
```

API сервиса будет доступен по адресу http://127.0.0.1:8000/

## Endpoints

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - документация Swagger
- [http://127.0.0.1:8000/russian_emotion_post/](http://127.0.0.1:8000/russian_emotion_post/) - ендпоинт для POST запросов. Пример:

### Запрос: 
```
{
    "text": "Счастье не за горами"
}
```

### Ответ:
```
{
    "results": [
        {
            "label": "happiness",
            "score": 0.9981801509857178
        },
        {
            "label": "neutral",
            "score": 0.0004348930960986763
        },
        {
            "label": "sadness",
            "score": 0.00039091211510822177
        },
        {
            "label": "enthusiasm",
            "score": 0.0003458599385339767
        },
        {
            "label": "anger",
            "score": 0.0002660590107552707
        },
        {
            "label": "fear",
            "score": 0.0002581431472208351
        },
        {
            "label": "disgust",
            "score": 0.0001240042911376804
        }
    ]
}
```
## Технологии:
- Python 3.10
- FastAPI
- uvicorn 
- torch
- transformers
