import json


def load_data(filepath):
    '''Loads data from json file'''
    with open(filepath, 'r') as handle:
        return json.load(handle)


def serialize_animal(animal) -> str:
    out_string = ''
    name = animal.get('name')
    characteristics = animal['characteristics']
    locations = animal['locations']

    out_string += '<li class="cards__item">'

    if name:
        out_string += f'<div class="card__title">{name}</div>\n'

    out_string += '<div class="card__text">\n'
    out_string += '<ul class="animal-details">'

    if characteristics.get("diet") is not None:
        out_string += f'<li class="animal-detail"><strong>Diet:</strong> {characteristics["diet"]}</li>\n'

    if locations:
        out_string += f'<li class="animal-detail"><strong>Location:</strong> {locations[0]}</li>\n'

    if characteristics.get('type') is not None:
        out_string += f'<li class="animal-detail"><strong>Type:</strong> {characteristics["type"]}</li>\n'
    out_string += '</ul>'
    out_string += '</div>'
    out_string += '</li>'
    return out_string


animals_data = load_data('animals_data.json')

skin_types = set()

for animal in animals_data:
    skin_type = animal["characteristics"].get("skin_type")
    if skin_type:
        skin_types.add(skin_type)

print("Available skin types:")
for skin_type in skin_types:
    print(skin_type)
print("All")

selected_skin_type = input("Enter a skin type: ").capitalize()

# open animals_template html and store it in template
with open("animals_template.html", 'r') as handle:
    template = handle.read()

# loop through json and store wanted data in output string
output: str = ""
for animal in animals_data:
    skin_type = animal["characteristics"].get("skin_type")
    if skin_type == selected_skin_type or selected_skin_type == "All":
        output += serialize_animal(animal)

# replace string in template with output and store in final_html
final_html = template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output
)

# write final_html to animals.html
with open("animals.html", 'w') as handle:
    handle.write(final_html)

