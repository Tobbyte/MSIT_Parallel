from random import randint
import matplotlib.pyplot as plt
from my_fuzzy_search import get_similar

""" A simple interface to interact with an dummy movie "db" (local dict) """

"""
Constraints imposed by the given task:
- Passing around the "db" is not fine and reassigning it in run() not strictly
  necessary, but done for clarity


TODO (but out of scope of this exercise):
  - unify input validation across features, f.e. update and add
  - add: check if already exists, present option to update
  - update: check if not existing, present option to add
  - delete: implement search
  - fix fail on empty db
  - add real clear terminal
  - implement fname from matplotlib instead naive str as filename
  - don't relay on exit()

  
Version 1.1.0
"""

"""
 ~~ Made with ❤️ and without ai or code completion (except intelliSense) ~~
"""


def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7,
    }

    run(movies)

"""dict used to shorthand color codes"""
colors = {
    "red": "\033[91m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "end": "\033[00m"
}

def sort_by_value(dic: dict[str, float], reverse=False):
    """
    Sorts a dict by its values
    TODO:
        - save sorted dict, update on add/remove
    """

    return sorted(dic.items(), key=lambda item: item[1], reverse=reverse)


def list_movies(db: dict[str, float], message, descending=False, by_value=False):
    """Returns a list of all db items"""

    output(message, space_before=True)
    if not by_value:
        for k, v in db.items():
            output(f"{k}: {v}")
    else:
        for k, v in sort_by_value(db, reverse=descending):
            output(f"{k}: {v}")


def is_num(inp: str):
    """Validates if a sting input is a valid number"""

    if inp == "":
        return False
    try:
        float(inp)
    except ValueError:
        return False
    return True


def user_input(promt:str):
    inp = input(colors["yellow"] + promt)
    print("" + colors["end"], end="") # reset input coloring
    return inp

def add_movie(db):
    """Adds an item to db."""

    name = None
    rating = None

    while name is None or name == "":
        name = user_input("\nEnter new movie name: ")
        if name == "":
            output("Name required", color="red")

    while rating is None or rating == "":
        rating = user_input("Enter new movies rating (0-10): ")
        if rating == "":
            output("Rating required", color="red")
        elif not is_num(rating):
            rating = None
            output("Rating must be a number", color="red")
        elif float(rating) > 10:
            rating = None
            output("Rating must be between 0 - 10", color="red")

    db[name] = float(rating)

    output(f'Movie "{name}" with rating {rating} successfully added', space_before=True)
    return db


def del_movie(db: dict[str, float]):
    """Removes an item from db"""

    tbdeleted = None

    while tbdeleted is None or tbdeleted == "":
        tbdeleted = user_input("\nEnter movie name to delete: ")
        if tbdeleted == "":
            output("Name required", color="red")
        try:
            del db[tbdeleted]
            output(f'Movie "{tbdeleted}" successfully deleted', space_before=True)

            return db

        except KeyError:
            output(f"Movie {tbdeleted} doesn't exist!", space_before=True, color="red")
            break
    return db


def update_movie(db: dict[str, float]):
    """Updates db item."""
    tbupdated = None
    new_rating = None

    while tbupdated is None or tbupdated == "":
        tbupdated = user_input("\nEnter movie name to update: ")
        if tbupdated == "":
            output("Name required", color="red")
        try:
            db[tbupdated]
        except KeyError:
            output(f"Movie {tbupdated} doesn't exist!", space_before=True, color="red")
            return db

    while new_rating is None or new_rating == "":
        new_rating = user_input("Enter new movies rating (0-10): ")
        if new_rating == "":
            output("Rating required", color="red")
        elif not is_num(new_rating):
            new_rating = None
            output("Rating must be a number", color="red")
        elif float(new_rating) > 10:
            new_rating = None
            output("Rating must be between 0 - 10", color="red")

    output(
        f'Movie "{tbupdated}" successfully updated to rating: {new_rating}',
        space_before=True,
    )
    return db


def get_average(nums: list[float]):
    """returns average"""
    return sum(nums) / len(nums)


def get_median(nums: list[float]):
    """
    returns median
    TODO:
        - use import statistics
    """

    sorted_nums = sorted(nums)
    if len(sorted_nums) % 2 != 0:
        return sorted_nums[len(sorted_nums) // 2]
    else:
        centeri = len(sorted_nums) // 2
        return get_average(sorted_nums[centeri - 1 : centeri + 1])


def get_statistics(db: dict[str, float]):
    """
    Gets statistic:
    - average
    - median
    - top-ranked items
    - bottom-ranged items
    """

    val_list = list(db.values())
    vals_sorted = sort_by_value(db)

    avg = get_average(val_list)
    median = get_median(sorted(val_list))
    best_name, best_rat = vals_sorted[-1]
    worst_name, worst_rat = vals_sorted[0]

    output(f"Average rating: {avg}", space_before=True)
    output(f"Median rating: {median}")
    output(f'Best movie: "{best_name}", {best_rat}')
    output(f'Worst movie: "{worst_name}", {worst_rat}')


def get_random(db):
    """Returns random movie"""

    name, rating = list(db.items())[randint(0, len(db) - 1)]
    output(f"Your movie for tonight: {name}, it's rated {rating}", space_before=True)


def search_movie(db: dict[str, float]):
    """Searches for items. Not case sensitive"""
    orig_inp = None
    while orig_inp == None or orig_inp == "":
        orig_inp = user_input("\nEnter part of movie name: ")
        if orig_inp == "":
            output("Name required", color="red")

    inp = orig_inp.lower()
    search_results = fuzzy_search(db, inp)

    found_titles = [(found, db.get(found)) for (found, _) in search_results]

    if not found_titles:
        output(f'No Movie name similar to "{orig_inp}" (remember that at least the first letter has to match):\n', color="red")
    else:
        output(f'Movie titles similar to "{orig_inp}":\n', space_before=True)
        for name, rate in found_titles:
            output(f"{name}, {rate}")


def fuzzy_search(db: dict[str, float], search_term: str):
    """Fuzzy searches on term. Results sorted by distance"""

    similarity_threshold = 15
    titles = list(db.keys())

    similar_titles = get_similar(titles, search_term, similarity_threshold)

    return similar_titles


def ratings_histogram(db: list[float]):
    """Saves a mathplotlob histogram to disk"""

    filename = None
    plt.hist(db)
    while filename is None or filename == "":
        filename = user_input("Enter filename (saved as png unless otherwise specified): ")
        if filename == "":
            output("Filename required", color="red")
        elif not filename.isalpha():
            output("Filename must be alphanumeric", color="red")
            filename = None
        else:
            try:
                plt.savefig(filename)
                output(
                    f'File "{filename}" successfully saved to disk.', space_before=True
                )
            except ValueError:
                # TODO: - check on other exceptions (f.e. no write permission)
                # from mathplotlob:
                output(
                    "Format 'asd' is not supported (supported formats: avif, eps, gif, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff, webp)", color="red")


def idle_after_input():
    """Idles with prompt to continue"""
    user_input("\npress Enter to continue ")


def present_menu(menu_items: list[str]):
    """Prints the menu to the user, asks for input."""
    """ Options: 
  1. List movies, no input. Print. Return to menu.
  2. Add movie, single input:
    - str, int:[1-10] (not validated). Print new Entry. Return to menu.
  3. Delete movie, single input:
    - str. Print error or confirmation. Return to menu.
  4. Update movie, multi input:
      1.: str. Print error if not found. Return to menu.
      2.: int:[1-10] (not validated). Print new Entry. Return to menu.
  5. Stats, no input. Print. Return to menu.
  6. Random movie, no input. Print. Return to menu.
  7. Search movie, single input:
    - str. Print error or results. Return to menu.
  8. List movies sorted descending, no input. Print. Return to menu.
  9. Create ratings histogram
  0. Exit.
  """

    output("", space_before=True)

    for item in menu_items:
        output(item, color="blue")
    selection = None
    insist_to_quite = False
    while selection is None:
        selection = user_input("\nEnter choice (1-9): ")

        if len(selection) > 1 or not selection.isdecimal():
            if not insist_to_quite:
                output(
                    "Invalid input (Enter 0 - 9. Try again).\nOr press ENTER again to quit", color="red"
                )
                selection = None
                insist_to_quite = True
            else:
                quit_program()

    return int(selection)


def quit_program():
    exit()


def clear_screen():
    """Clear console hack"""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def output(any, color = None, space_after=False, space_before=False):
    """Prints what's given. Optionally adds gap or color"""

    if space_before:
        print("\n \n")
    if color:
        if color == "red":
            print(colors["red"] + any + colors["end"])
        if color == "blue":
            print(colors["blue"] + any + colors["end"])
        if color == "yellow":
            print(colors["yellow"] + any + colors["end"])
        else:
            color = None
    else:
        print(any)

    if space_after:
        print("\n \n")


def run(db: dict[str, float]):
    """Prints welcome and loops menu"""

    output("********** My Movies Database **********", space_before=True, color="blue")

    menu_items = [
        "Menu:",
        "1. List movies",
        "2. Add movie",
        "3. Delete movie",
        "4. Update movie",
        "5. Stats",
        "6. Random movie",
        "7. Search movie",
        "8. Movies sorted by rating",
        "9. Create ratings histogram",
        "0. Quit",
    ]

    while True:
        clear_screen()
        selection = present_menu(menu_items)

        if selection == 0:
            output("Goodbye")
            quit_program()

        clear_screen()
        output(f"~~~~~~~~~~\nSelected menu item: {menu_items[selection]}\n~~~~~~~~~~", color="yellow")
        if selection == 1:
            """ list """
            list_movies(db, f"{len(db)} movies in total:\n")
        elif selection == 2:
            """ add """
            db = add_movie(db)
        elif selection == 3:
            """ delete """
            db = del_movie(db)
        elif selection == 4:
            """ update """
            db = update_movie(db)
        elif selection == 5:
            """ stats """
            get_statistics(db)
        elif selection == 6:
            """ random """
            get_random(db)
        elif selection == 7:
            """ search """
            search_movie(db)
        elif selection == 8:
            """ list by rating """
            list_movies(db, "Movies by rating:\n", descending=True, by_value=True)
        elif selection == 9:
            """ histogram """
            ratings_histogram(list(db.values()))

        idle_after_input()


if __name__ == "__main__":
    main()
