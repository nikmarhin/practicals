
total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for {} items is ${:.2f}".format(number, total))