
# also known as "anonymous functions" - an alternative way to write a function, provided that 
# the function contains a single return (and no other statements)

# Look at 3 things:

# 1) Basic lamdba functions
# 2) Naming lambda functions
# 3) Multiple arguments

# def cube(number: float) -> float:

#     return number ** 3

cube = lambda x: x ** 3

# test this
print(cube(4))

# lambda function to return someone's full name
full_name = lambda first_name, last_name: first_name + " " + last_name

# call this
print(full_name("Andy","Brown"))