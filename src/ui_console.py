"""
Module: ui_console.py
Author: Erdem Vural
Last Modified by: Erdem Vural
Date Last Modified: 2025-12-10
Program Description:
    Console-based user interface for the sentiment analysis tool.
    This module provides a simple text menu that allows the user to:
        - analyze a single comment,
        - analyze multiple comments in a batch,
        - view a summary of positive, neutral, and negative results.

Revision History:
    2025-12-09 - Initial skeleton created.
    2025-12-10 - Improved input validation, output formatting, and documentation.
"""

from typing import List

from sentiment_model import analyze_sentiment, analyze_batch, summarize_batch
from preprocessing import clean_text, clean_comments


def run_app() -> None:
    """
    Main loop for the console-based user interface.

    Shows the main menu, handles user choices (single analysis,
    batch analysis, or exit), and calls the appropriate helper functions.
    """
    while True:
        print("\n=== Sentiment Analysis Tool ===")
        print("1) Analyze a single comment")
        print("2) Analyze multiple comments (one per line, end with empty line)")
        print("0) Exit")

        choice = input("Select an option (0, 1, or 2): ").strip()

        # Validate menu choice
        if choice == "1":
            handle_single_comment()
        elif choice == "2":
            handle_multiple_comments()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please enter 0, 1, or 2.")


def handle_single_comment() -> None:
    """
    Handle the flow for analyzing a single user comment.

    Asks the user to enter a comment, applies preprocessing,
    calls the sentiment model, and prints a formatted result.
    """
    print("\n--- Single comment analysis ---")
    text = input("Enter your comment: ")

    # Check for empty input
    if not text.strip():
        print("Please enter a non-empty comment.")
        return

    # Preprocess and analyze
    cleaned = clean_text(text)
    label = analyze_sentiment(cleaned)

    # Show detailed result
    print("\nResult:")
    print(f'  Original: "{text}"')
    print(f'  Cleaned : "{cleaned}"')
    print(f"  Sentiment: {label}")


def handle_multiple_comments() -> None:
    """
    Handle the flow for analyzing multiple comments in a batch.

    Reads comments line by line until the user enters an empty line,
    applies preprocessing to all comments, runs batch sentiment analysis,
    and prints both detailed results and a summary.
    """
    print("\n--- Batch comment analysis ---")
    print("Enter comments (one per line). Submit an empty line to finish.")

    lines: List[str] = []

    # Read comments until an empty line is entered
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    # If no comments were entered, inform the user and return to the menu
    if not lines:
        print("No comments entered. Returning to main menu.")
        return

    # Preprocess comments and perform batch analysis
    cleaned_comments = clean_comments(lines)
    results = analyze_batch(cleaned_comments)
    summary = summarize_batch(results)

    # Print detailed results
    print("\n=== Batch analysis results ===")
    for original, item in zip(lines, results):
        sentiment = item["sentiment"]
        print(f'- "{original}" -> {sentiment}')

    # Print summary in a readable format
    print("\nSummary:")
    print(f"  Positive: {summary.get('positive', 0)}")
    print(f"  Neutral : {summary.get('neutral', 0)}")
    print(f"  Negative: {summary.get('negative', 0)}")


if __name__ == "__main__":
    # Allow running this module directly for quick testing.
    run_app()
