def int_check(question):
	while True:
		try:
			response = int(input(question))
			if response <= 5:
				print("You are too young to to de doing this by yourself")
			break
		except ValueError:
			print("Not a valid age")
	return response

age = int_check("Enter your age!")
