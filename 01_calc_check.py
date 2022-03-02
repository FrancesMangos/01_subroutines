def ask_num(question):
    start = False
    while not start:
        try:
            num = int(input("Enter a number:"))
            start = True
        except ValueError:
            print("Please enter a number")

num1 = ask_num("Enter a number")
num2 = ask_num("Enter another number")

start = False
while not start:
    try:
        symbol = input("Would you like to +, -, * or / ?")
        if symbol == "-":
            answer = num1 - num2
        elif symbol == "*":
            answer = num1 * num2
        elif symbol == "+":
            answer = num1 + num2
        elif symbol == "/":
            answer = num1 / num2
        else:
            print("Please enter a valid sign")
    except ValueError:
        print("Please enter a valid sign")

print("{} {} {} = {}".format(num1, symbol, num2, answer))
