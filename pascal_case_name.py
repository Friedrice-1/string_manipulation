# ask the user to input their full name in incorrect casing

name = input("Please input your name in random casing: ")

# format to pascal case
pascal_name = name.title().replace(" ", "")
# print output
print(pascal_name)