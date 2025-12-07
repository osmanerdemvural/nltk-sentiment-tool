"""
Module: sentiment_model.py
Author: Erdem Vural
Last Modified by: Erdem Vural
Date Last Modified: 2025-12-07
Program Description:
    Provides sentiment analysis functions using NLTK VADER.
    It can analyze a single text or a batch of comments and
    return labels such as 'positive', 'negative', or 'neutral'.

Revision History:
    2025-12-07 - Initial version created with basic sentiment functions.
"""

from typing import List, Dict
from nltk.sentiment import SentimentIntensityAnalyzer

# Global analyzer instance
_sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of a single text string.

    Parameters:
        text (str): The input text to analyze.

    Returns:
        str: One of 'positive', 'negative', or 'neutral'.
    """
    if not text or text.strip() == "":
        return "neutral"

    scores = _sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.2:
        return "positive"
    elif compound <= -0.2:
        return "negative"
    else:
        return "neutral"


def analyze_batch(comments: List[str]) -> List[Dict[str, str]]:
    """
    Analyze a list of comments and return a list of results.

    Parameters:
        comments (List[str]): List of comment strings.

    Returns:
        List[Dict[str, str]]: Each item contains:
            {
                "text": original comment,
                "sentiment": 'positive'/'negative'/'neutral'
            }
    """
    results: List[Dict[str, str]] = []

    for c in comments:
        label = analyze_sentiment(c)
        results.append({
            "text": c,
            "sentiment": label
        })

    return results


def summarize_batch(results: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Create a simple summary from batch sentiment results.

    Parameters:
        results (List[Dict[str, str]]): Output from analyze_batch.

    Returns:
        Dict[str, int]: Counts of each sentiment type.
            Example: {"positive": 10, "neutral": 5, "negative": 3}
    """
    summary = {"positive": 0, "neutral": 0, "negative": 0}

    for r in results:
        label = r.get("sentiment", "neutral")
        if label in summary:
            summary[label] += 1

    return summary


if __name__ == "__main__":
    sample_comments = [
        "I love this product, it works perfectly!",
        "It is okay, nothing special.",
        "This is terrible, I hate it."
    ]

    batch_results = analyze_batch(sample_comments)
    for item in batch_results:
        print(f"Text: {item['text']}")
        print(f"Sentiment: {item['sentiment']}")
        print("-" * 40)

    print("Summary:", summarize_batch(batch_results))