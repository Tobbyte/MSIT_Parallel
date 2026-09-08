"""Functions for constructing HTML from data."""

from get_from_nested_object import get_from_nested_dict
from helpers import catch_empty_fields

CARD_FIELDS_STYLE = """.card__fields {
  list-style: none;
  padding-left: 0;
  margin: 0.5em 0 0;
}"""

CARD_FIELD_ITEM_STYLE = """.card__field-item {
  margin-bottom: 0.3em;
}"""


CARD_FIELD_OPEN = "<li class='card__field-item'>"
CARD_FIELD_CLOSE = "</li>"
CARD_ITEM_OPEN = "<li class='cards__item'>"
CARD_ITEM_CLOSE = "</li>"
CARD_TITLE_OPEN = "<div class='card__title'>"
CARD_TITLE_CLOSE = "</div>"
CARD_BODY_OPEN = "<div class='card__text'>"
CARD_BODY_CLOSE = "</div>"
CARD_LIST_OPEN = "<ul class='card__fields'>"
CARD_LIST_CLOSE = "</ul>"
STRONG_OPEN = "<strong>"
STRONG_CLOSE = "</strong>"


def serialize_fields(data: list, fields: list) -> str:
    """Output parts of db.

    First item of fields becomes title.
    """
    output = ""

    for d in data:
        datapoints = get_from_nested_dict(
            d,
            fields,
            first_occurrence_only=True,
        )

        output += get_card_object(catch_empty_fields(datapoints), fields[0])
    return output


def get_card_object(card_items: dict, title_field: str) -> str:
    """Turn one animal's datapoints into a title + field-list card.

    For lazy defensiveness and good measures it stringifies every item.
    Only first location should be shown.
    """
    title_content = ""
    field_items = ""
    for k, item in card_items.items():
        if str(k) == title_field:
            title_content = str(item)
        else:
            if item and isinstance(item, list):
                item = str(item[0])  # noqa: PLW2901 ok for here

            field_items += get_field_item(str(k).capitalize(), str(item))

    return get_card_item(
        get_card_title(title_content) + get_card_body(field_items),
    )


def get_field_item(label: str, value: str) -> str:
    """Wrap field item in li."""
    return (
        CARD_FIELD_OPEN
        + get_strong(label + ":")
        + " "
        + value
        + CARD_FIELD_CLOSE
    )


def get_card_item(data: str) -> str:
    """Wrap content in a card list item."""
    return CARD_ITEM_OPEN + data + CARD_ITEM_CLOSE


def get_card_title(data: str) -> str:
    """Wrap content in a card title div."""
    return CARD_TITLE_OPEN + data + CARD_TITLE_CLOSE


def get_card_body(data: str) -> str:
    """Wrap content in a card body in list."""
    return (
        CARD_BODY_OPEN
        + CARD_LIST_OPEN
        + data
        + CARD_LIST_CLOSE
        + CARD_BODY_CLOSE
    )


def get_strong(data: str) -> str:
    """Wrap content in a strong tag."""
    return STRONG_OPEN + data + STRONG_CLOSE


def update_template(html: str, addendum: str) -> str:
    """Inject cards and css into the template placeholder.

    TODO: Failsave against no style found.
    """
    style_tags_end = html.find("</style>") - 1
    html = (
        html[:style_tags_end]
        + CARD_FIELDS_STYLE
        + "\n"
        + CARD_FIELD_ITEM_STYLE
        + "\n"
        + html[style_tags_end:]
    )

    return html.replace("__REPLACE_ANIMALS_INFO__", addendum)
