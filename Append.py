# Write a program to add an item (entered by the user) to the end of the list.
# Create a list named odd_numbers with items 1, 3, and 5.
# Take an integer as input and assign it to number variable.
# Use the append() function to add user input item to the end of the list.
# Print the updated list.

odd_numbers = [1, 3, 5]
number = int(input("Enter the no:"))
odd_numbers.append(number)
print(odd_numbers)
