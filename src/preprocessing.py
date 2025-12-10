"""
Module: preprocessing.py
Author: Erdem Vural
Last Modified by: Erdem Vural
Date Last Modified: 2025-12-09
Program Description:
    Text preprocessing utilities for the sentiment analysis tool.
    This module cleans raw text (lowercase, remove punctuation,
    remove stopwords, etc.) before sending it to the sentiment model.

Revision History:
    2025-12-09 - Initial version with basic cleaning functions.
"""
from typing import List
import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Make sure required NLTK data is downloaded:
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# Global stopwords set
STOP_WORDS = set(stopwords.words("english"))
# Keep "not" as a meaningful word (important for sentiment)
STOP_WORDS.discard("not")


def clean_text(text: str) -> str:
    """
    Clean a single text string.

    Steps:
        - convert to lowercase
        - tokenize into words
        - remove punctuation tokens
        - remove English stopwords
        - join tokens back into a single string

    Parameters:
        text (str): raw input text

    Returns:
        str: cleaned text
    """
    if not text:
        return ""

    # 1) Lowercase
    text = text.lower().strip()

    # 2) Tokenize
    tokens = word_tokenize(text)

    # 3) Prepare helpers
    punctuation_set = set(string.punctuation)

    cleaned_tokens: List[str] = []

    for token in tokens:
        # Skip punctuation
        if token in punctuation_set:
            continue

        # Skip stopwords (like "the", "and", "is", etc.)
        if token in STOP_WORDS:
            continue

        cleaned_tokens.append(token)

    # 4) Join tokens back to string
    return " ".join(cleaned_tokens)


def clean_comments(comments: List[str]) -> List[str]:
    """
    Apply clean_text to a list of comments.

    Parameters:
        comments (List[str]): list of raw comment strings

    Returns:
        List[str]: list of cleaned comment strings
    """
    return [clean_text(c) for c in comments]


if __name__ == "__main__":
    # Simple manual test
    sample = "This is a SIMPLE example, with some STOPWORDS and PUNCTUATION!!!"
    print("Original: ", sample)
    print("Cleaned : ", clean_text(sample))