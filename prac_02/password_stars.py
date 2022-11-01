"""
CP1404/CP5632 - Practical 2 - Password stars
"""

min_length = 2
max_length = 6


def main():
    print("Please enter a valid password")
    print("Your password must be between", min_length, "and", max_length,
          "characters:")
    password = get_password()
    print_password(password)


def print_password(password):
    print("Your password is", "*" * len(password))


def get_password():
    password = input("Enter password: ")
    if len(password) < min_length or len(password) > max_length:
        print("Invalid password")
        password = input("Enter password: ")
    return password


main()