"""My Zootopia"""

import data_fetcher

# ANIMALS_DATA_PATH = "animals_data.json"
ANIMALS_TEMPLATE_PATH = "animals_template.html"
OUTPUT_PATH = "animals.html"
ENABLE_SKIN_TYPE_FILTER = False


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
            f"{characteristics['diet']}</li>\n"
        )

    if locations:
        out += (
            f'<li class="animal-detail"><strong>Location:</strong> '
            f"{locations[0]}</li>\n"
        )

    if characteristics.get("type") is not None:
        out += (
            f'<li class="animal-detail"><strong>Type:</strong> '
            f"{characteristics['type']}</li>\n"
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
    animals_data: list[dict], template: str, selected_skin_type: str, animal_name: str
) -> str:
    """Create final HTML content."""
    output = ""
    if not animals_data:
        output = f'<p>No animals found for "{animal_name}".</p>'
    else:
        for animal in animals_data:
            skin_type = animal["characteristics"].get("skin_type")

            if skin_type != selected_skin_type and selected_skin_type != "All":
                continue
            output += serialize_animal(animal)

    return template.replace(
        "__REPLACE_ANIMALS_INFO__",
        output,
    )


def load_template(template_path: str) -> str:
    """Load HTML template from file."""
    try:
        with open(template_path, encoding="utf-8") as file:
            template = file.read()
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Template file not found: {template_path}") from error

    return template


def save_html(filepath: str, final_html: str) -> None:
    """Save final HTML content to output file."""
    try:
        with open(
            filepath,
            "w",
            encoding="utf-8",
        ) as file:
            file.write(final_html)
            print(f"Website was successfully generated to the file {OUTPUT_PATH}.")
    except OSError as error:
        raise OSError(f"Could not write output file: {filepath}") from error


def prompt_skin_type(skin_types: set[str]) -> str:
    """Prompt the user until they enter a valid skin type or 'All'."""
    valid_choices = skin_types | {"All"}

    print("Available skin types:")
    for skin_type in sorted(skin_types):
        print(skin_type)
    print("All")

    while True:
        selected = input("Enter a skin type: ").strip().capitalize()
        if selected in valid_choices:
            return selected
        print(f"'{selected}' is not a valid option. Please try again.")


def main() -> None:
    """Run the Zootopia application."""
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)
    if ENABLE_SKIN_TYPE_FILTER:
        skin_types = get_skin_types(animals_data)
        selected_skin_type = prompt_skin_type(skin_types)
    else:
        selected_skin_type = "All"

    template = load_template(ANIMALS_TEMPLATE_PATH)
    final_html = create_animals_html(
        animals_data,
        template,
        selected_skin_type,
        animal_name
    )

    save_html(OUTPUT_PATH, final_html)


if __name__ == "__main__":
    main()
