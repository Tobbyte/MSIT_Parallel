"""Functions for loading and saving HTML template files."""

from pathlib import Path

from config import LOAD_FROM_PATH, SAVE_TO_PATH


def save_file(data: str) -> None:
    """Write the finished HTML to the template file."""
    try:
        with Path.open(
            SAVE_TO_PATH,
            "w",
            encoding="utf-8",
        ) as t_file:
            t_file.write(data)
        print("Website was successfully saved as animals_template.html.")
    except OSError as e:
        print(f"Error saving file: {e}")


def load_template() -> str:
    """Load the raw HTML template from backup file."""
    try:
        with Path.open(
            LOAD_FROM_PATH,
            encoding="utf-8",
        ) as t_file:
            return t_file.read()
    except OSError as e:
        print(f"Error loading template: {e}")
        raise
