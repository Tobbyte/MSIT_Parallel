# ruff: noqa: FIX002, TD002, TD003
"""Generate an animals overview HTML page from JSON data.

Bonus: Overkill on avoiding hardcoding JSON data fields. ;)

Version 2.0.0. <- submitted

~ Made with ❤️ and without ai or code completion (except intelliSense) ~


Todo:
    - extract error messages
    - sanitize data before injecting.

"""

import requests
from config import DEFAULT_ANIMAL_FIELDS
from data_fetcher import fetch_data
from file_handler import load_template, save_file
from get_from_nested_object import get_from_nested_dict
from helpers import (
    flattn_to_set,
    get_ab_choice,
    get_user_choice_from_list,
    get_user_input,
)
from html_constructor import (
    serialize_fields,
    update_template,
)


def my_zootopia() -> None:
    """Load, inject, save HTML animals.

    Prompts user for an animal name, fetches data from API,
    optionally filters by skin type.
    """
    animal_choice = get_user_input("Enter a name of an animal: ")

    try:
        animals_data = fetch_data(animal_choice)

    except requests.RequestException as e:
        print(f"There was an error requesting the data: {e}")

    else:
        if not animals_data:
            print(f"""The animal "{animal_choice}" doesn't exist""")

        else:
            print(f"Got {len(animals_data)} {animal_choice}-ish animals.")

            if get_ab_choice("Filter by skin type? [(y)es, (n)o]: ", "y", "n"):
                skin_types = flattn_to_set(animals_data, "skin_type")

                skin_choice = get_user_choice_from_list(
                    f"Choose your favorite skin type: {list(skin_types)}: ",
                    list(skin_types),
                )

                animals_data = list(
                    # TODO: simplify! Add smth. like a "get_simple_list"
                    # parameter to get_from_nested_dict response
                    filter(
                        lambda animal: (
                            next(
                                iter(
                                    next(
                                        iter(
                                            get_from_nested_dict(
                                                [animal],
                                                ["skin_type"],
                                            )["skin_type"],
                                        ),
                                        {},
                                    ).values(),
                                ),
                                "",
                            )
                            in (skin_choice, "n.n.")
                        ),
                        animals_data,
                    ),
                )

                print(
                    f"Got {len(animals_data)} animals with "
                    f"skin type '{skin_choice}'. Generating HTML.",
                )

            str_data = serialize_fields(animals_data, DEFAULT_ANIMAL_FIELDS)
            try:
                updated_html = update_template(load_template(), str_data)
            except OSError:
                print(
                    "Could not generate the site because the "
                    "template couldn't be loaded.",
                )
            else:
                save_file(updated_html)


if __name__ == "__main__":
    my_zootopia()
