# Create a program to create a list of first n natural numbers using list comprehension.

# Take an integer input from the user and assign it to n.
# Use list comprehension to create a list with items from 1 to n.
# Print the list.
# Assumption: We will assume that the user will always enter a positive integer.

n = int(input("Enter the no:"))
new = []
new = [i for i in range(1, n+1)]
print(new)
