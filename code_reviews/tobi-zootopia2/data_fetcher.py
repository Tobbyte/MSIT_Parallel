"""Module for handling API requests to the API Ninjas service."""

import time
from json import JSONDecodeError

import requests
from config import animals_endpoint, headers, url


def _get_with_retry(  # noqa: PLR0913
    url: str,
    endpoint: str,
    headers: dict,
    params: dict,
    retries: int = 3,
    delay: int = 2,
    timeout: int = 10,
) -> requests.Response:
    """Make a GET request with retries on connection errors."""
    for attempt in range(retries):
        try:
            response = requests.get(
                url + endpoint,
                headers=headers,
                params=params,
                timeout=timeout,
            )
            response.raise_for_status()

        except requests.exceptions.ConnectionError as e:
            # api-ninjas fails intermitting via dns over tls.
            print(f"Attempt {attempt + 1}")
            if attempt < retries - 1:
                time.sleep(delay)
            err_msg = (
                "A connection error occurred; "
                f"Failed after {retries} attempts: {e}"
            )

        except requests.exceptions.HTTPError as e:
            print(f"A HTTP error occurred: {e}")
            raise
        except requests.exceptions.RequestException as e:
            print(f"A request error occurred: {e}")
            raise

        else:
            return response

    raise requests.RequestException(err_msg)


def fetch_data(animal_name: str) -> list:
    """Fetch the animals data for the animal 'animal_name'.

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
    params_search_by_name = {"name": animal_name}

    with _get_with_retry(
        url,
        animals_endpoint,
        headers,
        params_search_by_name,
    ) as r:
        response_json_list = []
        try:
            response_json_list = r.json()
            if response_json_list and not isinstance(
                response_json_list[0],
                dict,
            ):
                raise TypeError  # noqa: TRY301
        except JSONDecodeError as e:
            print(f"Response body does not contain valid json: {e}")
        except TypeError:
            print("API returned unexpected file format.")
        return response_json_list
