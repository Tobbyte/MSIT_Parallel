import random
import statistics
import matplotlib.pyplot as plt

# A small program designed to browse and edit a movie database.

menu_options = ("Menu:",
                "1. List movies",
                "2. Add movie",
                "3. Delete movie",
                "4. Update movie",
                "5. Stats",
                "6. Random movie",
                "7. Search movie",
                "8. Movies sorted by rating",
                "9. Create Rating-Histogram")

movie_dict = {"The Shawshank Redemption": 9.5,
                "Pulp Fiction": 8.8,
                "The Room": 3.6,
                "The Godfather": 9.2,
                "The Godfather: Part II": 9.0,
                "The Dark Knight": 9.0,
                "12 Angry Men": 8.9,
                "Everything Everywhere All At Once": 8.9,
                "Forrest Gump": 8.8,
                "Star Wars: Episode V": 3.6}


def sort_single_values():

    # returned a sorted list of all the current values for the ratings
    # (each value appears only once)

    value_list = list(movie_dict.values())
    single_values = list(set(value_list))
    sorted_values = sorted(single_values, reverse=True)
    return sorted_values


def valid_users_choice(value):

    # check if user input is a number and in range

    try:
        value = int(value)
        if 1 <= value <= 9:
            return True
    except ValueError:
        return False


def valid_user_rating(value):

    # check if user input is a number and in range

    try:
        value = int(value)
        if 0<= value <= 10:
            return True
    except ValueError:
        return False


def valid_movie_name(name):

    # check that user input is not empty

    name = name.replace(" ","")
    if name != "":
        return True
    else:
        return False


def welcome():
    print("********** My Movies Database **********")


def menu():

    # print the menue

    for option in menu_options:
        print(option)


def list_movie():

    # List all the movies.
    # The distinction between “no movies,” “one movie,” and “many movies”
    # is just to ensure the grammar is correct—whether singular or plural.

    print()
    count = len(movie_dict)

    if count == 0:
        print("No movie available")
    elif count == 1:
        print(f"{count} movie in total")
    else:
        print(f"{count} movies in total")

    for movie in movie_dict:
        print(f"{movie}: {movie_dict[movie]}")


def add_movie():

    # Adds a new movie entry with a rating.
    # Checks that the movie has a name
    # and that the rating is within the allowed range.
    # Does not check whether the movie exists or is spelled correctly.

    new_movie = input("Enter new movie name: ")
    while not valid_movie_name(new_movie):
        new_movie = input("You have to enter a name: ")

    new_rating = input("Enter movie rating (0-10): ")
    while not valid_user_rating(new_rating):
        new_rating = input("Enter one number between 0 and 10: ")

    movie_dict[new_movie] = float(new_rating)

    if new_movie in movie_dict:
        print(f"Movie {new_movie} successfully added")

    # I know the last two lines aren't necessary.
    # I just want to check here to make sure no errors
    #   occurred during the add process and only display the success message
    #   if it actually worked.


def delete_movie():

    # Deletes a movie if it is in the database.
    # Checks whether a movie title has been entered.
    # Only works if the names match exactly.

    movie_name = input("Enter movie name to delete: ")
    while not valid_movie_name(movie_name):
        movie_name = input("You have to enter a name: ")

    if movie_name in movie_dict:
        del movie_dict[movie_name]
    else:
        print(f"Movie {movie_name} doesn't exist!")

    if movie_name not in movie_dict:
        print(f"Movie {movie_name} successfully deleted")

    # I know the last two lines aren't necessary.
    # I just want to check here to make sure no errors
    #   occurred during the deletion process and only display the success message
    #   if it actually worked.


def update_movie():

    # Updates a movie rating.
    # Checks whether a movie title was entered and
    # whether the new rating is within the allowed range.
    # Updates only if the movie is in the database.

    movie_name = input("Enter movie name: ")
    while not valid_movie_name(movie_name):
        movie_name = input("You have to enter a name: ")

    if movie_name in movie_dict:
        new_rating = float(input("Enter new movie rating (0-10) "))
        while not valid_user_rating(new_rating):
            new_rating = input("Enter one number between 0 and 10: ")
        movie_dict[movie_name] = float(new_rating)

        if movie_dict[movie_name] == float(new_rating):
            print(f"Movie {movie_name} successfully updated")
        # I know the last two lines aren't necessary.
        # I just want to check here to make sure no errors

    else:
        print(f"Movie {movie_name} does not exist!")


def stats_movie():
    average = sum(movie_dict.values()) / len(movie_dict)
    print(f"Average rating: {average}")

    median = statistics.median(movie_dict.values())
    print(f"Median rating: {median}")

    max_ranting = sort_single_values()[0]
    best_movies = []
    for movie, rating in movie_dict.items():
        if rating == max_ranting:
            best_movies.append(movie)
    if len(best_movies) == 1:
        print(f"Best movie: {best_movies[0]}, {movie_dict[best_movies[0]]}")
    else:
        print(f"Best movies with {movie_dict[best_movies[0]]}")
        for movie in best_movies:
            print(f"    {movie}")

    min_ranting = sort_single_values()[-1]
    worst_movies = []
    for movie, rating in movie_dict.items():
        if rating == min_ranting:
            worst_movies.append(movie)
    if len(worst_movies) == 1:
        print(f"Worst movie: {worst_movies[0]}, {movie_dict[worst_movies[0]]}")
    else:
        print(f"Worst movies with {movie_dict[worst_movies[0]]}")
        for movie in worst_movies:
            print(f"    {movie}")


def random_movie():

    # Returns a random movie with a rating,
    # but only if the database is not empty

    if len(movie_dict) == 0:
        print("No movie available")

    movie_list = list(movie_dict)
    suggested_movie = random.choice(movie_list)
    print(f"Your movie for tonight: {suggested_movie}, it's rated {movie_dict[suggested_movie]}")


def search_movie():

    # Printed the titles in the database that matches with the user's input.

    part = input("Enter part of movie name: ").strip().lower()
    for movie, rating in movie_dict.items():
        normalized_movie = movie.lower()
        if part in normalized_movie:
            print(f"{movie}: {rating}")


def sorted_movie():

    # Displays a list of movies sorted by rating

    sorted_values = sort_single_values()
    for value in sorted_values:
        for movie, rating in movie_dict.items():
            if rating == value:
                print(f"{movie}: {movie_dict[movie]}")


def histogram():
    pass


def users_choice(num):

    # Takes valid numbers and then assigns them to the function call.
    # Incorrect input is not possible here
    # because it was previously returned to the user

    if num == 1:
        list_movie()
    elif num == 2:
        add_movie()
    elif num == 3:
        delete_movie()
    elif num == 4:
        update_movie()
    elif num == 5:
        stats_movie()
    elif num == 6:
        random_movie()
    elif num == 7:
        search_movie()
    elif num == 8:
        sorted_movie()
    elif num == 9:
        histogram()


def main():
    welcome()
    want_continue = True
    while want_continue:
        print()
        menu()
        print()
        user_choice = input("Enter choice (1-9): ")
        while not valid_users_choice(user_choice):
            user_choice = input("Please select a valid option. Just one number between 1 and 9): ")
        users_choice(int(user_choice))
        print()
        user_input = input("Press any Enter to continue ")
        if user_input != "":
            want_continue = False
    print("Ok, see you")


if __name__ == '__main__':
    main()

