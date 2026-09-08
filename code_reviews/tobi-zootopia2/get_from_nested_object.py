"""A module to get values from a nested dict or list structure.

Expects structures as found from JSON, with dicts, lists, and tuples
(no sets or generators).
Exposes a single function get_from_nested_dict() that returns a dict of
all occurrences of keys in a nested structure,
annotated with the path to each occurrence.
"""

from collections.abc import Iterable


def _get_iterables(container: Iterable) -> list[tuple]:
    """Return a list of iterables, if any, annotated with index."""
    if isinstance(container, dict):
        iterables = container.items()
    elif isinstance(container, (tuple, list)):
        iterables = zip(range(len(container)), container, strict=False)
    else:  # sets or generators shouldn't be possible from JSON, but defensive.
        return []
    return [(i, v) for i, v in iterables if isinstance(v, (list, tuple, dict))]


def _get_from_nested_dict(
    container: dict | list | tuple,
    key_names: set[str],
    found_keys: dict | None = None,
    parent: tuple = (),
    *,
    first_occurrence_only: bool = False,
) -> dict | None:
    """Recurse a nested object, return path and values or None.

    Args:
        container: Dict or list to search
        key_names: Set of keys to find
        found_keys: Dictionary tracking found keys
        parent: Tuple tracking the path to the current container
        first_occurrence_only: If True, stop searching after first
        occurrence of each key

    Returns:
        Dictionary with found keys and their paths, or None

    """
    found_keys = found_keys if found_keys is not None else {}

    if isinstance(container, dict):
        # look for keys in this level
        for k in container.keys() & key_names:
            if first_occurrence_only:
                found_keys[k] = container[k]
                key_names = key_names - found_keys.keys()
                if not key_names:
                    return found_keys
            else:
                found_keys.setdefault(k, []).append({parent: container[k]})

    # get nested iterables and annotate with "parent"
    for nested_item in _get_iterables(container):
        current_parent_name = nested_item[0]
        found_keys = _get_from_nested_dict(
            nested_item[1],
            key_names,
            found_keys,
            (*parent, current_parent_name),
            first_occurrence_only=first_occurrence_only,
        )
        if first_occurrence_only and found_keys:
            key_names = key_names - found_keys.keys()
            if not key_names:
                break

    return found_keys


def get_from_nested_dict(
    container: dict | list,
    key_names: list[str],
    *,
    first_occurrence_only: bool = False,
) -> dict:
    """Find key_names anywhere in a nested structure.

    Returns a dict with every occurrence of key from key_names as dict
    with list of dicts of tuple of paths: value | None if not found.
    Results on root level have empty tuple as path.
    Returns in order of of keynames.


    Returns:
        dict[str: list[dict[tuple[str | int]: value]]]
        {
            "key_name":
                [
                    {
                        ((),): value_on_root
                    },
                    {
                        (level1, level2): value_on_level2
                    }
                ]
        }

    """
    found_keys = (
        _get_from_nested_dict(
            container,
            set(key_names),
            first_occurrence_only=first_occurrence_only,
        )
        or {}
    )
    default_return = None if first_occurrence_only else []
    return {k: found_keys.get(k, default_return) for k in key_names}


if __name__ == "__main__":
    mockdata = {
        "name": "American Foxhound",
        "taxonomy": {
            "kingdom": "Animalia",
        },
        "locations": [
            "North-America",
        ],
        "characteristics": {
            "type": "Hound",
            "name": "name2",
            "sub": {"name": "name3"},
            "subList": ["a", {"name": "name4"}],
        },
    }
    res = get_from_nested_dict(
        mockdata,
        ["name", "asdasd", "type", "asd"],
        first_occurrence_only=True,
    )
    for k, v in res.items():
        print("res:", k, v)
