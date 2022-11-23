"""
Emails
Estimate: 45 minutes
Actual: 28 minutes
"""

my_dictionary = {}


def main():
    email = input("Email: ")
    while email != "":
        name = name_extractor(email)
        question = input(f"Is your name {name}? (Y/n) ")
        if question.upper() != "Y" and question != "":
            name = input("Name: ")
        my_dictionary[email] = name
        email = input("Email: ")

    for email, name in my_dictionary.items():
        print(f"{name} ({email})")


def name_extractor(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()