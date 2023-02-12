# Create a list using list comprehension and print the list.

# Take an integer input from the user and store it in variable n.
# Create a list of numbers from 1 to n using list comprehension.
# Print the list.

n = int(input("Enter the no:"))
numbers = [n for n in range(1, n+1)]
print(numbers)
