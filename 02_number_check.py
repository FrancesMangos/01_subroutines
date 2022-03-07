def int_check(question):
	while True:
		try:
			response = int(input(question))
			break
		except ValueError:
			print("Not a valid age")
	return response


age = int_check("Enter your age!")
if age >= 5:
    print("You are too young to to de doing this by yourself")

