start = False
while not start:
    try:
        num1 = int(input("Enter a number:"))
        start = True
    except ValueError:
        print("Please enter a number!")

start_num = False
while not start_num:
    try:
        num2 = int(input("Enter another number:"))
        start_num = True
    except ValueError:
        print("Please enter a number!")

start_symbol = False
while not start_symbol:
    symbol = input("Would you like to: add? (+), subtract (-), multiply (*) or divide (/) ?")
    if symbol == "-":
        print("{} - {} = ".format(num1, num2))
        print(num1 - num2)
        start_symbol = True
    elif symbol == "+":
        print("{} - {} = ".format(num1, num2))
        print(num1 + num2)
        start_symbol = True
    elif symbol == "/":
        print("{} / {} = ".format(num1, num2))
        print(num1 / num2)
        start_symbol = True
    elif symbol == "*":
        print("{} * {} = ".format(num1, num2))
        print(num1 * num2)
        start_symbol = True
    else:
        print("Please enter a symbol!")

