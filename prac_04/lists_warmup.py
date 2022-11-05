numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])  # 3 - the first number in the list is the 0th number
print(numbers[-1])  # 2 - the last number in the list
print(numbers[3])  # 1 - the 4th number in the list, as it starts at 0
print(numbers[:-1])  # -  slice the list from the 0th number to the last number, output should be [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # - slice the list from the 3rd to the 4th number, output should be [1]
print(5 in numbers)  # - is there 5 records within the list, yes, so True
print(7 in numbers)  # - 7th number which doesn't exist so False
print("3" in numbers)  # - asking if "3" exists in numbers as a string, which will be false
print(numbers + [6, 5, 3])  # - append the list with 6, 5 ,3 - new list will be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1.         Change the first element of numbers to "ten" (the string, not the number 10)
numbers.insert(1, 'ten')
print(numbers)

# 2.         Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3.         Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4.         Print whether 9 is an element of numbers
wanted_numeral = 9
if wanted_numeral in numbers:
    print("Yes, 9 is in there!")
else:
    print("Nope, no 9!")