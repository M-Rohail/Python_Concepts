# Write a program to create a function that can take a variable number of keyword arguments.

# Create a function named full_name() that can take a variable number of keyword arguments.
# Inside the function, print the arguments.
# Outside the function

# Take two string inputs and assign them to variables first and last respectively.
# Call the full_name() function like this: full_name(first = first, last = last)
def full_name(**ptr):
    for i, value in ptr.items():
        print(ptr)


first = input("Enter the no:")
last = input("Enter the no:")
full_name(first=first, last=last)
