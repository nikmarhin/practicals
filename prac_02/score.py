"""
CP1404 - Practical 2
"""

import random


def main():
    result = ""
    score = float(input("Enter score: "))
    get_result(score)
    print(result)
    print(random.randint(0, 100))


def get_result(score):
    result = ""
    while score < 0 or score > 100:
        result = "Invalid score"
        if score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"
    return result


main()
