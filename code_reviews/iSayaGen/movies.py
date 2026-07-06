"""This module handles a movie database CLI application."""

import random


def list_movies(movies):
    print("\n------------ Movie List ------------\n")
    for title, rating in movies.items():
        print(f"{title}: {rating}")
    print("\n------------------------------------")


def add_movie(movies):
    """Prompt the user to add a new movie with a rating (0–10) to the collection."""
    title = input("\nEnter movie title (leave empty to cancel): ").strip()

    if not title:
        print("\nCancelled by user.")
        return

    if title in movies:
        print("\nMovie already exists!")
        return

    while True:
        rating_input = input("\nEnter rating (0-10) or 'exit' to cancel: ")

        if rating_input.lower() == "exit":
            return

        try:
            rating = float(rating_input)

            if 0 <= rating <= 10:
                break
            else:
                print("\nRating must be between 0 and 10.")

        except ValueError:
            print("\nInvalid rating. Please enter a number")
            return

    movies[title] = rating
    print("\n------------------------------------\n")
    print(f"Movie '{title}' was added successfully!")
    print("\n------------------------------------")


def delete_movie(movies):
    """Allow the user to delete a movie from the collection by name or index."""
    if not movies:
        print("\nNo movies to delete.")
        return

    movie_list = list(movies.keys())

    print("\nSelect a movie to delete:")
    for i, title in enumerate(movie_list, start=1):
        print(f"{i}. {title}")

    while True:
        choice = input("\nEnter movie number or 'exit' to cancel: ")

        if choice.lower() == "exit":
            return

        # Option 1: User enters a number
        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(movie_list):
                title = movie_list[index]
            else:
                print("\nInvalid number.")
                continue

        # Option 2: User enters a title
        else:
            # Case-insensitive match
            matches = [t for t in movie_list if t.lower() == choice.lower()]

            if matches:
                title = matches[0]
            else:
                print("\nMovie not found.")
                continue

        confirm = input(f"\nDelete '{title}'? (y/n): ")

        if confirm.lower() == "y":
            del movies[title]
            print("\n------------------------------------\n")
            print(f"Movie '{title}' deleted successfully!")
            print("\n------------------------------------")
        else:
            print("\nDeletion canceled.")
        return


def select_movie(movies):
    """Prompt the user to select a movie from the list by number or name."""
    movie_list = list(movies.keys())

    print("------------------------------------\n")
    print("Select a movie to update:\n")

    for i, title in enumerate(movie_list, start=1):
        print(f"{i}. {title} ({movies[title]})")

    print("\n------------------------------------\n")

    while True:
        choice = input("Enter movie number, name or 'exit' to cancel: ")

        if choice.lower() == "exit":
            return None

        # Option 1: number input
        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(movie_list):
                return movie_list[index]
            else:
                print("\nInvalid number.")
                continue

        # Option 2: title input (case-insensitive)
        matches = [t for t in movie_list if t.lower() == choice.lower()]

        if matches:
            return matches[0]
        else:
            print("\nMovie not found.")


def get_rating():
    """Prompt the user for a valid movie rating between 0 and 10, or exit."""
    while True:
        rating_input = input("\nEnter new rating (0-10) or 'exit': ")

        if rating_input.lower() == "exit":
            return None

        try:
            rating = float(rating_input)

            if 0 <= rating <= 10:
                return rating
            else:
                print("\nRating must be between 0 and 10.")

        except ValueError:
            print("\nInvalid rating. Please enter a number.")


def update_movie(movies):
    """Update the rating of an existing movie selected from the list by number or name."""
    if not movies:
        print("\nNo movies available.")
        return

    title = select_movie(movies)

    if title is None:
        return

    rating = get_rating()

    if rating is None:
        return

    movies[title] = rating

    print("\n------------------------------------\n")
    print(f"Updated successfully!\nNew rating of '{title}' is {rating}")
    print("\n------------------------------------")


def show_stats(movies):
    """Display statistics about the movie collection (average, median, best, worst)."""
    if not movies:
        print("\nNo movies available.")
        return

    # Extract ratings for statistical calculations
    ratings = list(movies.values())

    average = sum(ratings) / len(ratings)

    best_rating = max(ratings)
    worst_rating = min(ratings)
    # Find all movies matching best/worst rating (handles ties)
    best_movies = [title for title, rating in movies.items() if rating == best_rating]
    worst_movies = [title for title, rating in movies.items() if rating == worst_rating]

    sorted_ratings = sorted(ratings)
    n = len(sorted_ratings)

    # Median depends on odd/even number of elements
    if n % 2 == 1:
        median = sorted_ratings[n // 2]
    else:
        median = (sorted_ratings[n // 2 - 1] + sorted_ratings[n // 2]) / 2

    print("\n-------------- Stats ---------------\n")
    print(f"Average rating: {average:.2f}")
    print(f"Median rating: {median:.2f}")
    print(f"Best movie(s): {', '.join(best_movies)} ({best_rating})")
    print(f"Worst movie(s): {', '.join(worst_movies)} ({worst_rating})")
    print("\n------------------------------------")


def random_movie(movies):
    """Display a randomly selected movie from the collection."""
    if not movies:
        print("\nNo movies available.")
        return

    title = random.choice(list(movies.keys()))
    rating = movies[title]

    print("\n----------- Random Movie -----------\n")
    print(f"{title}: {rating}")
    print("\n------------------------------------")


def search_movies(movies):
    """Search for movies by title substring (case-insensitive)."""
    if not movies:
        print("\nNo movies available.")
        return

    query = input("\nEnter search term: ").lower()

    results = []

    for title, rating in movies.items():
        if query in title.lower():
            results.append((title, rating))

    if not results:
        print("\nNo matching movies found.")
        return

    print("\n---------- Search results ----------\n")
    for title, rating in results:
        print(f"{title} ({rating})")
    print("\n------------------------------------")


def sorted_movies(movies):
    """Display all movies sorted by rating in descending order."""
    if not movies:
        print("\nNo movies available.")
        return

    # Sort by second tuple element (rating)
    sorted_list = sorted(movies.items(), key=lambda item: item[1], reverse=True)
    print("\n------ Movies sorted by rating -----\n")
    for title, rating in sorted_list:
        print(f"{title}: {rating}")
    print("\n------------------------------------")


def pause():
    """Pause program execution until the user presses Enter."""
    input("\nPress Enter to continue...")


def main():
    """Run the main menu loop for the movie database CLI application."""
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

    print("\n\n********** Movie Database **********")

    while True:
        print("\n============== Menu: ===============\n")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movies")
        print("8. Movies sorted by rating")
        print("9. Exit")
        print("\n====================================")

        choice = input("\nChoose an option: ")

        if choice == "9":
            print("\nGoodbye!\n")
            break
        elif choice == "1":
            list_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            update_movie(movies)
        elif choice == "5":
            show_stats(movies)
        elif choice == "6":
            random_movie(movies)
        elif choice == "7":
            search_movies(movies)
        elif choice == "8":
            sorted_movies(movies)
        else:
            print("\nInvalid choice, try again.")
        pause()


if __name__ == "__main__":
    main()
