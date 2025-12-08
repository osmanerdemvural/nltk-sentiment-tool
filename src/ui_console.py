"""
Module: ui_console.py
Author: Fazlur Rahman
Last Modified by: Fazlur Rahman
Date Last Modified: 2025-12-07
Program Description:
    Simple console-based user interface for the sentiment analysis tool.
    Provides a menu for single and batch analysis.

Revision History:
    2025-12-07 - Initial skeleton created.
"""

from typing import List
from sentiment_model import analyze_sentiment, analyze_batch, summarize_batch
from preprocessing import clean_text, clean_comments


def run_app() -> None:
    """
    Main loop for the console UI.
    """
    while True:
        print("\n=== Sentiment Analysis Tool ===")
        print("1) Analyze a single comment")
        print("2) Analyze multiple comments (one per line, end with empty line)")
        print("0) Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            handle_single_comment()
        elif choice == "2":
            handle_multiple_comments()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


def handle_single_comment() -> None:
    text = input("\nEnter your comment: ")
    cleaned = clean_text(text)
    label = analyze_sentiment(cleaned)
    print(f"Sentiment: {label}")


def handle_multiple_comments() -> None:
    print("\nEnter comments (one per line). Submit an empty line to finish.")
    lines: List[str] = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    cleaned = clean_comments(lines)
    results = analyze_batch(cleaned)
    summary = summarize_batch(results)

    print("\nResults:")
    for item in results:
        print(f"- \"{item['text']}\" -> {item['sentiment']}")

    print("\nSummary:", summary)
