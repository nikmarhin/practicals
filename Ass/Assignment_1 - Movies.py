"""
CP1404 2022 - Assignment 1
Movies To Watch 1.0
Student Name: Nikolas Marhin
Pseudocode:

MAIN_MENU = parent menu
MENU_CHOICES = list of menu choices
MOVIE_CATEGORIES = list of categories
movies_list = list of movies
watched_list = list of unwatched movies
UNWATCHED_MOVIES = len(movies_list) - len(watched_list)

main function
    display intro message
    load cas and import movies into movies list
    display main menu
    get user choice
    while user choice is not quit
        if user choice is display
            run display function
            repeat menu
        elif user choice is to add
            run add movie function
        elif user choice is watch
            run watch movie function
    else
        display farewell message
        write current movie list to file and save file


define watch menu function
    display intro message to the watch menu
    get user input for movie number
    if number is less than 1 or more than length of movie list
        display error
        repeat input
    else
        append user input to watched movie list
        display movie has been watched


define display report function
    i = 0
    for movie in movies list
        display iterate through movies list to display all elements
        display x movies watched, x movies still to watch - referencing the constant of UNWATCHED_MOVIES


define add movie function
    create a blank list for 'movie'
    get title input from user
        if title is blank display error
    get year input from user
        error check it is a valid input, ie. more than 0 and must be an integer
    display categories list, referencing CATEGORIES constant
    get category input from user
    if category input is not in CATEGORIES constant display error
        repeat category input from user
    append title, year, category to blank movie list
    append movies list with movie
    append watched list with movie
    display movie added to list


define get valid menu choice function
    get user input
    while user input is not in MENU CHOICES, referencing constant
        display error
        repeat user input
    return user choice
"""


MAIN_MENU = "D - Display movies \nA - Add new movie \nW - Watch a movie \nQ - Quit"
MENU_CHOICES = ["D", "A", "W", "Q"]
MOVIE_CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
movies_list = [["Jurassic Park", 1996, "Action"], ["The Stranger", 2022, "Drama"], ["Interstellar", 2018, "Sci-Fi"]]
watched_list = []
UNWATCHED_MOVIES = len(movies_list) - len(watched_list)


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
        elif user_choice == "A":
            add_movie()
            print(MAIN_MENU)
            user_choice = get_valid_menu_choice()
        elif user_choice == "W":
            watch_menu()
            print(MAIN_MENU)
            user_choice = get_valid_menu_choice()
    else:
        print("Have a nice day :)")
        # saves the movies to the CSV file, overwriting file contents
        # display report for movies watched and print("x movies saved to movies.csv")


def watch_menu():
    """Mark a movie as watched"""
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
    """Display the current movie list"""
    i = 0
    for movie in movies_list:
        row = movie
        print(str(i + 1) + ". "
              + "{:20}".format(row[0])
              + "{:2}".format("-")
              + "{:^6}".format(str(row[1]))
              + "({})".format(str((row[2]))))
        i += 1
    print(f"{(len(watched_list))} movies watched {UNWATCHED_MOVIES} movies still to watch")
    return None


def add_movie():
    """Add movie to the movies list"""
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
    watched_list.append(movie)
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
