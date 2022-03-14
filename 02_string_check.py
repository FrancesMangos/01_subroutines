def int_check(question):
	while True:
		try:
			response = int(input(question))
			if response >= 5:
			    return response

			print("You are too young to to de doing this by yourself")
		except ValueError:
			print("Not a valid age")


def check_input(question):
    while True:
        try:
            response = input(question).title()
            if response.isdigit() or response == "" or response.isdecimal():
                print("That is not a valid name")
            else:
                return response
        except ValueError:
            print("Not valid name")

age = int_check("Enter your age:")
name = check_input("Enter your name:")

print("So your name is {} and you are {} years old?".format(name, age))

