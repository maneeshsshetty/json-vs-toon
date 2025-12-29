# JSON vs TOON Comparison App

A simple Flask application that demonstrates the difference between **JSON** (JavaScript Object Notation) and **TOON** (Token-Oriented Object Notation).

The app reads character data from `data.json`, converts it to the token-efficient TOON format using `toon-python`, and displays both formats side-by-side for easy comparison.

## Features

- **Side-by-Side Comparison:** View the standard JSON output next to the compact TOON output.
- **Dynamic Conversion:** Data is converted on-the-fly, ensuring the comparison is always up-to-date.
- **Flask Backend:** A lightweight Python web server powers the application.

## Prerequisites

- Python 3.10+
- `pip` (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/maneeshsshetty/json-vs-toon.git
    cd json-vs-toon
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # macOS/Linux
    source env/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install flask toon-python
    ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000/`.

## File Structure

- `app.py`: The main Flask application handling the logic and rendering.
- `data.json`: The source data containing a list of cartoon characters.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## About TOON Format

TOON is designed to be a more token-efficient serialization format for LLMs (Large Language Models), reducing token usage while maintaining human readability.
