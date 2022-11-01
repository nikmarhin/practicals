"""
CP1404 - Practical 2
"""

import random


def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    print(random.randint(0, 100))


def get_result(score):
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
