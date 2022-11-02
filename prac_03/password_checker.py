"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("Enter password: ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Enter password: ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    if len(password) >= MIN_LENGTH and len(password) <= MAX_LENGTH:
        for char in password:
            if char.islower:
                count_lower += 1
            else:
                print("Your password must contain a lower case letter")
        for char in password:
            if char.isupper:
                count_upper += 1
            else:
                print("Your password must contain an upper case letter")
        for char in password:
            if char.isdigit:
                count_digit += 1
            else:
                print("Your password must contain a number")
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special += 1
            else:
                print("Your password must contain a special character")
                SPECIAL_CHARS_REQUIRED = True
    pwd_length: int = count_lower + count_upper + count_digit + count_special
    if count_lower >= 1 and count_upper >= 1 and count_digit >= 1 and count_special >= 1 and (pwd_length > MIN_LENGTH and pwd_length < MAX_LENGTH):
        print(f"Valid password = {password}")



    # for char in password:
    #     # TODO: count each kind of character (use str methods like isdigit)
    #     pass



    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    # return True


main()

# if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
#     print(f"Your password must be between, {MIN_LENGTH}, and, {MAX_LENGTH}")
# elif not password.islower():
#     print("Your password must contain a lower case letter")
# elif not password.isupper():
#     print("Your password must contain a capital letter")
# elif not password.isdigit():
#     print("Your password must contain a number")
# elif not password.isupper():
#     print("Your password must contain a capital letter")
# else:
#     print("Your new password has been approved")