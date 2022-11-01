"""
CP1404 - Practical 2
"""

GAME_MENU = "(G)et a valid score (must be 0-100 inclusive), (P)rint result, (S)how stars, (Q)uit"
MENU_CHOICES = ["G", "P", "S", "Q"]


def main():
    print(GAME_MENU)
    player_choice = get_valid_menu_choice()
    # return get_valid_menu_choice()
    return player_choice
    while player_choice != "Q":
        if player_
    score = float(input("Enter score: "))
    print(get_result(score))
    print("Your score is", "*" * len(score))


def get_valid_menu_choice():
    """Get a valid menu choice from the user."""
    player_choice = input("Choose: ").upper()
    while player_choice not in MENU_CHOICES:
        print("Invalid choice")
        player_choice = input("Choose: ").upper()
    return player_choice


def get_result(score):
    """Get a valid score, with error checking"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
