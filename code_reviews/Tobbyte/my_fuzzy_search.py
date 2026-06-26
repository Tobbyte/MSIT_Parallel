"""Custom Fuzzy Search implementation using naive Levenshtein algorithm"""

"""
Limitations:
    - expects at least any first char of search term matching comp items
    - doest not optimize search in any meaningful way
    - when searching f.e. for "the" not all results containing "the" are returned, results are still restricted by distance.
"""

"""
 ~~ Made with ❤️ and without ai or code completion (except intelliSense) ~~
"""

"""
TODO:
  - extend excluded_terms list (now only "the")
  - make checking for first letter matching optional
  - retry without checking for first letter matching if no results
  - extend docstrings by what fn is used for
"""

__all__ = ["get_similar"]  # public method

# terms to be excluded from search term or comparison items
excluded_terms = ["the"]


def _print_fuzzy_table(table: list, str1: str, str2: str):
    """Pretty print the table"""

    header = str1
    column = str2

    first_col_w = len(column)
    cell_w = len(header)

    # header Row
    header_row: list[str] = ["_"]
    for i in range(len(header)):
        header_row.append(header[: i + 1])

    # body rows
    display_rows: list[list[str | int]] = []
    original_row: list[int | str] = []

    for i, original_row in enumerate(table):
        row_copy = list(original_row)
        row_prefix = "_" if i == 0 else column[:i]
        row_copy.insert(0, row_prefix)
        display_rows.append(row_copy)

    print("")

    # Print header Row
    print("▦".rjust(first_col_w), end="")
    # Align to first data column
    print(" " * (first_col_w + 1), end="")

    for cell in header_row:
        print(str(cell).ljust(cell_w + 1), end="")

    print("\n")

    # print data rows
    for row in display_rows:
        # first cell (row labels)
        print(str(row[0]).rjust(first_col_w), end=" ")

        for cell in row[1:]:
            print(str(cell).rjust(cell_w), end=" ")
        print("\n")


def _calc_distance(search_term: str, compar_term: str, print_table=False):
    """Calculates the distance between inputs"""

    data_matrix = _init_table(search_term, compar_term)

    for row in range(1, len(data_matrix)):
        for column in range(1, len(data_matrix[row])):
            left_cell = data_matrix[row][column - 1] + 1
            top_cell = data_matrix[row - 1][column] + 1
            diag_top_char = search_term[column - 1]
            diag_left_char = compar_term[row - 1]
            diag_is_diff = 0

            if diag_top_char != diag_left_char:
                diag_is_diff = 1
            diag = data_matrix[row - 1][column - 1] + diag_is_diff
            data_matrix[row][column] = min(left_cell, top_cell, diag)

    if print_table:
        print("\n\n\n\n\n\n")
        _print_fuzzy_table(data_matrix, search_term, compar_term)
        print(f"distance: {data_matrix[-1][-1]}")

    return data_matrix[-1][-1]


def _init_table(str1: str, str2: str):
    """Initializes the table for distance calculation"""

    data_matrix: list = []

    for i in range(0, len(str2) + 1):
        row = []
        for j in range(0, len(str1) + 1):  # len word + extra 0
            if i == 0:
                # top row
                row.append(j)
            else:
                if j == 0:
                    # left column
                    row.append(i)
                else:
                    row.append(-1)
        data_matrix.append(row)

    return data_matrix


def _term_is_excluded(term: str):
    """checks if the term is in excluded list"""
    return term.strip() in excluded_terms


def _strip_excluded_terms(term: str):
    """Strips any items from input that are in exclude list"""

    stripped = term

    # prevent excluding self
    if not _term_is_excluded(stripped):
        for exc in excluded_terms:
            stripped = stripped.replace(
                exc + " ", ""
            )  # add " " to find only at beginning

    return stripped


def _any_first_char_matching(term1: str, term2: str):
    """Checks if any word of the given strings begins with the first letter"""

    lterm1 = term1.split()
    lterm2 = term2.split()
    for w1 in lterm1:
        for w2 in lterm2:
            if w1 and w2 and w1[0] == w2[0]:
                return True
    return False


def get_similar(db: list[str], search_term: str, threshold: int, print_table=False):
    """
    Uses a basic Fussy Search over list:[str] of items and returns
    similar items to comparison term[str]. Takes a threshold for the distance calculation and optionally prints (every) table
    """

    search_term_wo_excluded = _strip_excluded_terms(search_term).lower()

    similar_results: list[tuple] = []
    for item in db:
        item_wo_excluded = item.lower()
        # prevent no results when search term is in excluded list
        if not _term_is_excluded(search_term):
            item_wo_excluded = _strip_excluded_terms(item.lower())

        dist = _calc_distance(
            search_term_wo_excluded, item_wo_excluded, print_table=print_table
        )

        # naively demand first char matching
        if dist <= threshold and _any_first_char_matching(
            search_term_wo_excluded, item_wo_excluded
        ):
            similar_results.append((item, dist))

    similar_results = sorted(similar_results, key=lambda dist: dist[1])
    return similar_results


if __name__ == "__main__":
    pass
