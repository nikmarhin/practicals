"""Assignment 1"""

MAIN_MENU = "D - Display movies \nA - Add new movie \nW - Watch a movie \nQ - Quit"
MENU_CHOICES = ["D", "A", "W", "Q"]
MOVIE_CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
movies_list = [["Jurassic Park", 1996, "Action"], ["The Stranger", 2022, "Drama"], ["Interstellar", 2018, "Sci-Fi"]]
watched_list = []


def main():
    print("Movies To Watch 1.0 - by Nik Marhin")
    # load csv and input movies into list
    print(MAIN_MENU)
    user_choice = get_valid_menu_choice()
    while user_choice != "Q":
        if user_choice == "D":
            display_movies()
            print(MAIN_MENU)
            user_choice = get_valid_menu_choice()
            # display a formatted (lined up) list of all the movies with their details (unwatched movies have * next to them) and a count of these movies
            # print(displayed movies report)
            # print(x movies watched, x movies still to watch)
        elif user_choice == "A":
            add_movie()
            print(MAIN_MENU)
            user_choice = get_valid_menu_choice()
        elif user_choice == "W":
            watch_menu()
            print(MAIN_MENU)
            user_choice = get_valid_menu_choice()
        # prompt the user to choose one movie by number (error-checked), then change that movie's status to watched
        # if no movies are unwatched, then display "No more movies to watch!"
    else:
        print("Have a nice day :)")
        # saves the movies to the CSV file, overwriting file contents
        # display report for movies watched and print("x movies saved to movies.csv")


def watch_menu():
    print("Enter the number of a movie to mark as watched")
    number = int(input(">>> "))
    if number < 1 or number > len(movies_list):
        print("Invalid movie number.")
        number = int(input(">>> "))
    else:
        movie = movies_list[number - 1]
        watched_list.append(movie)
        print(movie[0] + " watched")
    return None


def display_movies():
    i = 0
    for movie in movies_list:
        row = movie
        print(str(i + 1) + ". "
              + "{:20}".format(row[0])
              + "{:2}".format("-")
              + "{:^6}".format(str(row[1]))
              + "({})".format(str((row[2]))))
        i += 1
    return None


def add_movie():
    movie = []
    title = input("Title: ")
    if title == "":
        print("Input cannot be blank")
        title = input("Title: ")
    try:
        year = int(input("Year: "))
        while year < 1:
            print("Number must be >=1")
            year = int(input("Year: "))
    except ValueError:
        print("Invalid input, enter a valid number")
        # DOES NOT LOOP BACK TO TRY EXECUTION
    print("Categories available: Action, Comedy, Documentary, Drama, Thriller, Other")
    category = input("Category: ").capitalize()
    if category not in MOVIE_CATEGORIES:
        print("Invalid category; using Other")
        category = "Other"
        return category
    movie.append(title)
    movie.append(year)
    movie.append(category)
    movies_list.append(movie)
    print(movie[0] + f" ({category} from {year}) added to the movie list.")
    return None


def get_valid_menu_choice():
    """Get a valid menu choice from the user."""
    user_choice = input(">>>>> ").upper()
    while user_choice not in MENU_CHOICES:
        print("Invalid menu choice")
        user_choice = input(">>>>> ").upper()
    return user_choice


main()
