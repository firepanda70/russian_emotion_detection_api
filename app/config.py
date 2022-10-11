from pydantic import BaseSettings


DESCR = '''
Связано с моделью Animore.

[GitHub Модели](https://github.com/aniemore/Aniemore)

[Hugging Face](https://huggingface.co/Aniemore)
'''

TITLE = 'API для модели анализа тональности (sentiment analysis) предложения.'


class Settings(BaseSettings):
    app_title: str = TITLE
    app_description: str = DESCR
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
