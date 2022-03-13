def calc():
    while True:
        try:
            response = int(input("Which times table would you like to see?"))
            print()
            start = True
            print("Here is the {} times tables".format(response))
            for x in range(1, 13):
                answer = x * response
                print("{} times {} is {}".format(x, response, answer))
            return response
        except ValueError:
            print("Please enter a NUMBER!")

calc()
