"""Functions for handling user input and data manipulation."""

import sys

from get_from_nested_object import get_from_nested_dict


def catch_empty_fields(data: dict) -> dict:
    """Replace empty (none) field values with 'n.n.'."""
    return {k: v if v is not None else "n.n." for k, v in data.items()}


def flattn_to_set(data: list[dict], field: str) -> set:
    """Flatten the results of get_from_nested_dict() to set on field."""
    return {
        v
        for res in catch_empty_fields(
            get_from_nested_dict(data, [field]),
        )[field]
        for v in res.values()
    }


def get_user_input(prompt: str) -> str:
    """Get input from user."""
    insist_to_quit = None
    while (user_input := input(prompt)).strip() == "":
        if insist_to_quit:
            sys.exit()
        print("Input can't be empty.\n Press Enter again to quit.")
        insist_to_quit = True

    return user_input


def get_ab_choice(prompt: str, opt_a: str, opt_b: str) -> bool:
    """Ask user to choose between opt_a and opt_b.

    Returns True for opt_a,
    returns False for opt_b.
    """
    while True:
        choice = get_user_input(prompt)
        if choice not in (opt_a, opt_b):
            print(f'Choose "{opt_a}" or "{opt_b}": ')
        else:
            break

    return choice == opt_a


def get_user_choice_from_list(prompt: str, options: list) -> str:
    """Ask user to choose from a list of options."""
    while choice := get_user_input(prompt).strip():
        if choice not in options:
            print(f"Choose one of {options}")
        else:
            break
    return choice
