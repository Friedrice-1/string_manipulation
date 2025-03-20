# ask user to input a statement

statement = input("Please enter a statement: ")

# count words in that statement
word_count = len(statement.split())
# print result
print(f"There are {word_count} words.")