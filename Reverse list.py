# Write a program to reverse a given list.

# Create a list my_list and assign [1, 2, 3, 4] to it.
# Create a new list with items in the reverse order and print it.

# my_list = [1, 2, 3, 4]
# new_list = []
# new_list = my_list[::-1]
# print(new_list)

# New list Slicing
# Write a program to create a new list from an existing list using list slicing.

# Create a list named my_list with items 'p','r','o','g','r','a','m','i','z'.
# Use the slicing notation to get a new list from the second to the second-last items from my_list.
# Print the new list.

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
new_list = my_list[1:-1:1]
print(new_list)
