"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        user_bonus = sales * .15
        print(f"User bonus is: {user_bonus:.0f}")
        sales = float(input("Enter sales: $"))
    else:
        user_bonus = sales * .10
        print(f"User bonus is: {user_bonus:.0f}")
        sales = float(input("Enter sales: $"))
print("You entered a negative number, goodbye.")