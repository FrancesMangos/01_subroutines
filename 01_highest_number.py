
def highest(a, b):
    if a > b:
        highest_num = a
    else:
        highest_num = b
    print("The highest number is {}".format(highest_num))

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

highest(num1, num2)
