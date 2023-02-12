# Write a program to check if the first and last characters of a string are equal.
# Take string as input and assign it to check variable.
# Use list indexing to check if the first and the last character of a string are equal or not.
# If yes, print Equal. Else print Not Equal.

check = []
check = input("Enter the text:")

if check[0] == check[-1]:
    print("Equal")
else:
    print("Not Equal")
