NLTK-Based Sentiment Analysis Tool

A simple Python console application that analyzes the sentiment of user comments using NLTK VADER.
The tool classifies text as positive, neutral, or negative, and supports both single and batch analysis.

Features

Analyze the sentiment of a single comment

Analyze multiple comments in one run (batch mode)

Text preprocessing:

Lowercasing

Tokenization

Punctuation removal

English stopwords removal (while keeping important words like "not")

Sentiment classification using NLTK VADER

Color-coded output in the console (using colorama):

Green → positive

Yellow → neutral

Red → negative

Clear console menu with input validation and summary for batch results

Tech Stack

Language: Python 3.x

Libraries:

nltk (VADER sentiment, tokenization, stopwords)

colorama (for colored console output)

Interface: Console / terminal

Tools: Visual Studio Code, Git, GitHub

Installation

Clone the repository:

git clone https://github.com/osmanerdemvural/nltk-sentiment-tool.git
cd nltk-sentiment-tool


(Optional but recommended) Create and activate a virtual environment:

python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate


Install required libraries:

python -m pip install nltk colorama


Download the necessary NLTK data:

python -m nltk.downloader vader_lexicon punkt punkt_tab stopwords

Usage

Run the main entry point:

python src/main.py


You will see a menu like this:

=== Welcome to the Sentiment Analysis Tool ===

Menu:
  1) Analyze a single comment
  2) Analyze multiple comments (one per line, end with empty line)
  0) Exit

Option 1 – Single Comment

Choose 1

Type one sentence, for example:

Enter your comment: I love this product, it works perfectly!


The program will:

Clean the text

Analyze sentiment

Show the result, with the sentiment color-coded (green/yellow/red)

Option 2 – Multiple Comments (Batch)

Choose 2

Enter several comments, one per line

Press Enter on an empty line to finish

Example:

I love sunshine
It is okay, nothing special
I'm a bit nervous about my exam
This is terrible

[empty line here]


The program will:

Clean each comment

Analyze sentiment for each one

Print a numbered list of comments with their sentiment

Show a summary, for example:

Summary:
  Positive: 2
  Neutral : 1
  Negative: 1

Option 0 – Exit

Choose 0

The program will ask for confirmation:

Are you sure you want to exit? (y/n)


y → exit

n → return to the menu

Project Structure
nltk-sentiment-tool/
├── src/
│   ├── main.py              # Entry point, calls run_app()
│   ├── preprocessing.py     # Text cleaning functions
│   ├── sentiment_model.py   # Sentiment analysis and batch summary
│   └── ui_console.py        # Console UI, menu, input/output, color display
├── .gitignore
└── README.md