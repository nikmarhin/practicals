"""
CP1404 - Practical
"""



import random

print(random.randint(5, 20))  # line 1
# Code asks for a random number between 5 and 20, inclusive.
# The smallest number could be 5, the largest could be 20.

print(random.randrange(3, 10, 2))  # line 2
# Code asks for a random number within the range of 3 to 12, with a rule to increase by 2 every iteration.
# The smallest number could be 3, the largest could be 9. 4 is not possible as the output values must increase by 2.

print(random.uniform(2.5, 5.5))  # line 3
# Code asks for a random number within the range 2.5 and 5.5.
# The smallest number could be 2.5~~~ and the largest number could be 5.5. There is no rounding set so the output
# will show to 16 decimal places

print(random.randint(1, 100))
# Code that outputs a random number between 1 and 100, inclusive.
