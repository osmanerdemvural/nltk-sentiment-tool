# NLTK Sentiment Tool

Simple sentiment analysis tool using Python and NLTK (VADER).
This project is for our COMP final project.

## How to run

```bash
python -m pip install nltk
python -m nltk.downloader vader_lexicon
python src/sentiment_model.py

from sentiment_model import analyze_sentiment, analyze_batch, summarize_batch

text = "I love this product, it works perfectly!"
label = analyze_sentiment(text)
print(label)  # 'positive', 'neutral', or 'negative'

comments = [
    "I love this product, it works perfectly!",
    "It is okay, nothing special.",
    "This is terrible, I hate it."
]

results = analyze_batch(comments)
summary = summarize_batch(results)
print(summary)  # {'positive': X, 'neutral': Y, 'negative': Z}
