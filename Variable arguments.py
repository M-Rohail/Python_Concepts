# Create a function named print_items() that can take any number of arguments.

# Inside the function,

# use a for loop to print all the arguments passed during the function call
# Outside the function

# take two string inputs and store them in variables text1 and text2 respectively
# call the print_item() function with text1 as an argument
# call the print_item() function with text1 and text2 as arguments

# def print_items(*text):
#     for i in text:
#         print(i)


# text1 = input("Enter the text:")
# text2 = input("Enter the text:")
# print_items(text1)
# print_items(text1, text2)

# **kwags
# Create a program where a function can accept a variable number of keyword arguments.

# Create a function

# Create a function named greet() that can take a variable number of keyword arguments.
# Print the argument
# Outside the function

# Take two string inputs and assign it to variable formal and informal respectively.
# Call the greet() function like this: greet(formal = formal, informal = informal)

def greet(**any):
    print(any)


formal = input("Enter the no:")
informal = input("enter the no:")
greet(formal=formal, informal=informal)
