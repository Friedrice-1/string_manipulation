# ask user to input a number

num = int(input("Please enter a number between 1-1000s: "))

# format the number
formatted_num = str(num).zfill(6)
# print output
print(formatted_num)