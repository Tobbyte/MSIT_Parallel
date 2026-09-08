"""Configuration for Zootopia2."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    err_msg = "API Key not found in env."
    raise RuntimeError(err_msg)

url = "https://api.api-ninjas.com/v1/"

animals_endpoint = "animals"

headers = {
    "Accept": "application/json",
    "X-Api-Key": API_KEY,
}



PROJECT_ROOT = Path(__file__).resolve().parent  # project root
SAVE_TO_PATH = PROJECT_ROOT / Path("animals_template.html")
LOAD_FROM_PATH = PROJECT_ROOT / Path("animals_template_orig_backup.html")

DEFAULT_ANIMAL_FIELDS = [
    "name",
    "temperament",
    "diet",
    "locations",
    "type",
    "skin_type",
]
