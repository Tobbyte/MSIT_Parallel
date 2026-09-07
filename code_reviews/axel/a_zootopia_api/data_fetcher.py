"""Fetch amimals data from the API."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_data(animal_name: str) -> list[dict[str, object]]:
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    api_key = os.getenv("API_KEY")
    if api_key is None:
        raise ValueError("API_KEY is not set in the .env file")
    response = requests.get(
        f"https://api.api-ninjas.com/v1/animals?name={animal_name}",
        headers={"X-Api-Key": api_key},
    )
    if response.status_code == 200:
        return response.json()
    raise Exception(
        f"Failed to fetch data for {animal_name}. Status code: {response.status_code}"
    )
