"""
Module: ui_console.py
Author: Fazlur Rahman
Last Modified by: Fazlur Rahman
Date Last Modified: 2025-12-10
Program Description:
    Enhanced console-based UI for the sentiment analysis tool.
    Adds input validation, formatted output, and color-coded sentiment results.

Revision History:
    2025-12-07 - Initial skeleton created.
    2025-12-10 - Enhanced UI, input validation, formatting, comments, color output.
"""

from typing import List
from sentiment_model import analyze_sentiment, analyze_batch, summarize_batch
from preprocessing import clean_text, clean_comments
from colorama import init, Fore, Style

# Initialize colorama for Windows
init(autoreset=True)


def run_app() -> None:
    """
    Main loop for the console UI.
    Continuously shows the menu until the user chooses to exit.
    """
    print("=== Welcome to the Sentiment Analysis Tool ===")
    while True:
        print("\nMenu:")
        print("  1) Analyze a single comment")
        print("  2) Analyze multiple comments (one per line, end with empty line)")
        print("  0) Exit")

        choice = get_menu_choice()

        if choice == "1":
            handle_single_comment()
        elif choice == "2":
            handle_multiple_comments()
        elif choice == "0":
            confirm_exit = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm_exit == "y":
                print("Goodbye.")
                break
            else:
                print("Returning to menu...")


def get_menu_choice() -> str:
    """
    Prompt the user for a valid menu choice (0, 1, or 2).
    Repeats until a valid input is entered.

    Returns:
        str: the chosen option
    """
    valid_choices = {"0", "1", "2"}
    while True:
        choice = input("Select an option: ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please enter 0, 1, or 2.")


def colorize_sentiment(sentiment: str, text: str) -> str:
    """
    Return the text wrapped with color based on sentiment.

    Parameters:
        sentiment (str): 'positive', 'neutral', or 'negative'
        text (str): the comment text

    Returns:
        str: colored string for console display
    """
    if sentiment == "positive":
        return Fore.GREEN + text + Style.RESET_ALL
    elif sentiment == "negative":
        return Fore.RED + text + Style.RESET_ALL
    else:
        return Fore.YELLOW + text + Style.RESET_ALL


def handle_single_comment() -> None:
    """
    Prompt the user for a single comment, clean it,
    analyze the sentiment, and display the result with color.
    """
    text = input("\nEnter your comment: ").strip()
    if not text:
        print("No input detected. Returning to menu...")
        return

    cleaned = clean_text(text)
    label = analyze_sentiment(cleaned)

    print("\nResult:")
    print(f"  Comment   : {text}")
    print(f"  Sentiment : {colorize_sentiment(label, label.capitalize())}")


def handle_multiple_comments() -> None:
    """
    Prompt the user to enter multiple comments (one per line),
    clean them, analyze sentiment for each, and display results
    and summary statistics with colors.
    """
    print("\nEnter comments (one per line). Press Enter on an empty line to finish.")
    lines: List[str] = []

    while True:
        line = input().strip()
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("No comments entered. Returning to menu...")
        return

    cleaned = clean_comments(lines)
    results = analyze_batch(cleaned)
    summary = summarize_batch(results)

    print("\nResults:")
    for i, item in enumerate(results, start=1):
        sentiment_colored = colorize_sentiment(item['sentiment'], item['sentiment'].capitalize())
        print(f"{i}. Comment : \"{item['text']}\" | Sentiment: {sentiment_colored}")

    print("\nSummary:")
    for sentiment, count in summary.items():
        color = {
            "positive": Fore.GREEN,
            "neutral": Fore.YELLOW,
            "negative": Fore.RED
        }.get(sentiment, "")
        print(f"  {color}{sentiment.capitalize():<8}: {count}{Style.RESET_ALL}")