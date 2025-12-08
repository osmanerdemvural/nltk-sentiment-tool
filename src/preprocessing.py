"""
Module: preprocessing.py
Author: Jongwon Lee
Last Modified by: Jongwon Lee
Date Last Modified: 2025-12-07
Program Description:
    Text preprocessing utilities for the sentiment analysis tool.
    This module will clean raw text (lowercase, remove punctuation,
    remove stopwords, etc.) before sending it to the sentiment model.

Revision History:
    2025-12-07 - Initial skeleton created.
"""

from typing import List


def clean_text(text: str) -> str:
    """
    Clean a single text string.

    Steps (to be implemented):
        - convert to lowercase
        - remove extra spaces
        - (optionally) remove punctuation
        - (optionally) remove stopwords

    For now, this function just returns the original text.
    """
    # TODO: implement real cleaning logic
    return text


def clean_comments(comments: List[str]) -> List[str]:
    """
    Apply clean_text to a list of comments.
    """
    return [clean_text(c) for c in comments]
