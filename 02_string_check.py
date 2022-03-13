def int_check(question):
	while True:
		try:
			response = int(input(question))
			if response <= 5:
			    print("You are too young to to de doing this by yourself")
            else:
			    break
		except ValueError:
			print("Not a valid age")
    return response

def check_input(question):
    while True:
        try:
            response = input(question)
            if response.isdigit():
                print("That is not a valid name")
            else:
                break
        except ValueError:
            print("Not valid name")
    return response

age = int_check("Enter your age:")
name = check_input("Enter your name:")

print("So your name is {} and you are {} years old?".format(name, age))
