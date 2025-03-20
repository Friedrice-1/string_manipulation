# ask user to input their name

name = input("Please enter your name: ")

# check if there are spaces at the start and remove them
name = name.lstrip()
# print output
print(f"Output: {name}")