# ask the user to input their full name in incorrect casing

name = input("Please input your name in random casing: ")

# format to snake case
snake_name = name.lower().replace(" ", "_")
# print output
print(snake_name)