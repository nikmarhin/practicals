"""
CP1404 - Practical 2
"""

GAME_MENU = "(G)et a valid score, (P)rint result, (S)how stars, (Q)uit"
MENU_CHOICES = ["G", "P", "S", "Q"]


def main():
    game_result = ""
    print("Welcome, place make a selection:")
    print(GAME_MENU)
    player_choice = get_valid_menu_choice()
    while player_choice != "Q":
        if player_choice == "G":
            result = get_score()
            game_result = result
            print(GAME_MENU)
            player_choice = get_valid_menu_choice()
        elif player_choice == "P":
            if game_result == "":
                print("You haven't provided a score yet")
                game_result = get_score()
                print(evaluate_score(game_result))
            else:
                print("Your score is", evaluate_score(game_result))
                print(GAME_MENU)
                player_choice = get_valid_menu_choice()
        else:
            if game_result == "":
                print("You haven't provided a score yet")
                game_result = get_score()
            else:
                print(score_as_stars(game_result))
                print(GAME_MENU)
                player_choice = get_valid_menu_choice()
    print("Thank you, have a nice day!")


def score_as_stars(game_result):
    if game_result == "":
        print("You haven't provided a score yet")
        print(get_score)
    else:
        print("Your score is", "*" * len(game_result))


def get_valid_menu_choice():
    """Get a valid menu choice from the user."""
    player_choice = input("Choose: ").upper()
    while player_choice not in MENU_CHOICES:
        print("Invalid choice")
        player_choice = input("Choose: ").upper()
    return player_choice


def get_score():
    """Get a valid score"""
    result = int(input("Enter score: "))
    if result < 0 or result > 100:
        print("Invalid score")
        result = int(input("Enter score: "))
    return result


def evaluate_score(game_result):
    if game_result >= 90:
        outcome = "excellent"
    elif game_result >= 50:
        outcome = "passable"
    else:
        outcome = "bad"
    return outcome


main()
