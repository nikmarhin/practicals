"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? If an input is not an integer.
2. When will a ZeroDivisionError occur? If zero is entered as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    a) Add an if statement for the denominator input to error check if a 0 is entered
    b) Bypass the ZeroDivisionError with a 'try/except' statement, where the 'except'
       block sets the result variable to 0 - see below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    try:
        fraction = numerator / denominator
        print(fraction)
    except ZeroDivisionError:
        result = 0
        print(result)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")