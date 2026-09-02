"""My Zootopia."""

import json


ANIMALS_DATA_PATH = "animals_data.json"
ANIMALS_TEMPLATE_PATH = "animals_template.html"
OUTPUT_PATH = "animals_output.html"


def load_data(filepath: str) -> list[dict]:
    """Load data from JSON file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal: dict) -> str:
    """Serialize animal data into HTML string."""
    out = ""
    name = animal.get("name")
    characteristics = animal["characteristics"]
    locations = animal["locations"]

    out += '<li class="cards__item">'

    if name:
        out += f'<div class="card__title">{name}</div>\n'

    out += '<div class="card__text">\n'
    out += '<ul class="animal-details">'

    if characteristics.get("diet") is not None:
        out += (
            f'<li class="animal-detail"><strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if locations:
        out += (
            f'<li class="animal-detail"><strong>Location:</strong> '
            f'{locations[0]}</li>\n'
        )

    if characteristics.get("type") is not None:
        out += (
            f'<li class="animal-detail"><strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    out += "</ul>"
    out += "</div>"
    out += "</li>"

    return out


def get_skin_types(animals_data: list[dict]) -> set[str]:
    """Return all available skin types."""
    return {
        animal["characteristics"].get("skin_type")
        for animal in animals_data
        if animal["characteristics"].get("skin_type")
    }


def create_animals_html(
    animals_data: list[dict],
    template: str,
    selected_skin_type: str,
) -> str:
    """Create final HTML content."""
    output = ""

    for animal in animals_data:
        skin_type = animal["characteristics"].get("skin_type")

        if skin_type == selected_skin_type or selected_skin_type == "All":
            output += serialize_animal(animal)

    return template.replace(
        "__REPLACE_ANIMALS_INFO__",
        output,
    )


def main() -> None:
    """Run the Zootopia application."""
    animals_data = load_data(ANIMALS_DATA_PATH)

    skin_types = get_skin_types(animals_data)

    print("Available skin types:")
    for skin_type in sorted(skin_types):
        print(skin_type)
    print("All")

    selected_skin_type = input(
        "Enter a skin type: "
    ).strip().capitalize()

    with open(
        ANIMALS_TEMPLATE_PATH,
        "r",
        encoding="utf-8",
    ) as file:
        template = file.read()

    final_html = create_animals_html(
        animals_data,
        template,
        selected_skin_type,
    )

    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(final_html)


if __name__ == "__main__":
    main()

