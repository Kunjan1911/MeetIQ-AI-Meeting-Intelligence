from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):

    if len(text) > 512:
        text = text[:512]

    result = sentiment_pipeline(text)[0]

    return result