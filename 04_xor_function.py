def or_function(a, b):
    if a == True and b == True:
        c = False
        return c
    if a == False and b == False:
        c = False
        return c
    else:
        c = True
        return c

one = 4 == 4
two = 2 == 2

print(or_function(one, two))
