def main():
    numbers = []
    amount_of_inputs = 5
    for n in range(1, amount_of_inputs + 1):
        number = int(input(f"Enter a number {n}: "))
        numbers.append(number)
    for n in range(len(numbers)):
        print("Number: ", numbers[n])
    print("The first number is ", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is ", min(numbers))
    print("The largest number is ", max(numbers))
    print("The average of the numbers is ", sum(numbers) / len(numbers))
    #   Number: 5
    #   Number: 20
    #   Number: 1
    #   Number: 2
    #   Number: 3
    #   The first number is 5
    #   The last number is 3
    #   The smallest number is 1
    #   The largest number is 20
    #   The average of the numbers is 6.2
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_input = str(input("Enter a username: "))
    if user_input in usernames:
        print("Access granted!")
    else:
        print("Access denied")


main()