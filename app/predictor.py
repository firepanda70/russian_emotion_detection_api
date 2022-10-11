import torch
from transformers import BertForSequenceClassification, AutoTokenizer

LABELS = ['neutral', 'happiness', 'sadness', 'enthusiasm', 'fear', 'anger', 'disgust']
tokenizer = AutoTokenizer.from_pretrained('Aniemore/rubert-tiny2-russian-emotion-detection')
model = BertForSequenceClassification.from_pretrained('Aniemore/rubert-tiny2-russian-emotion-detection')


@torch.no_grad()
def predict_emotions(text: str) -> dict:
    """
        It takes a string of text, tokenizes it, feeds it to the model, and returns a dictionary of emotions and their
        probabilities
        :param text: The text you want to classify
        :type text: str
        :return: A sorted dictionary of emotions and their probabilities.
    """
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    emotions_list = {}
    for i in range(len(predicted.numpy()[0].tolist())):
        emotions_list[LABELS[i]] = predicted.numpy()[0].tolist()[i]
    return {k: v for k, v in sorted(emotions_list.items(), key=lambda item: item[1], reverse=True)}
