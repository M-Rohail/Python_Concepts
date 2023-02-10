# Create a list containing 3 items: 9, 11, and 15, and assign it to the odd_numbers variable.
# Print the second item of the list (using a positive index).

# odd_numbers = [9, 11, 15]
# print(odd_numbers[1])

# Create an empty list and assign it to the animals variable.
# Add 'dog' to the end of the animals list using the append() method.
# Print the animals list.
# Again add 'cat' to the animals list using the append() method.
# Print the animals list again.
# animals = []
# animals.append("dog")
# print(animals)
# animals.append("Cat")
# print(animals)

# The easiest way to find the number of items a list has is by using the built-in len() function.

# Can you find the length of a list without using this function?

# Suppose we have a list like this [10, 20, 30, 40]
# Your task is to find the length of this list programmatically.
# num = [10, 20, 30, 40]
# size = 0
# for i in num:
#     size = size+1

# print(size)

# Create a tuple containing 4 items: 9, 11, 15, 17 and assign them to the odd_numbers variable.
# Print the third item of the tuple (using a positive index).
# odd_numbers = (9, 11, 15, 17)
# print(odd_numbers[2])

# Assign the 'Snowpiercer' string to a variable named movie.
# Print the fourth character from the string (using a positive index).

# movie = "Snowpiercer"
# print(movie[3])

# Take two string inputs from the user and store them in text1 and text2 respectively.
# Create a new string that will contain the first four characters of the text1 string and the last four characters of the text2 string. Store the resultant string in the result variable.
# Print the new string.

# text1 = input("Enter the Text:")
# text2 = input("Enter the Text")
# result = text1[:4]+text2[-4:]
# print(result)

# Assign the dictionary below to a variable named prices.

# {'apple': 2.5, 'kiwi': 3.4}
# Then,

# Change the value of the 'apple' key to 3.5.
# Print the dictionary.
# Add an item (key: 'banana', value: 3) to the dictionary.
# Print the dictionary again.

# prices = {
#     "apple": 2.5,
#     "Kiwi": 3.4
# }
# prices["apple"] = 3.5
# print(prices)
# prices["banana"] = 3
# # print(prices)

# Assign the dictionary below to a variable named prices.
# {'apple': 2, 'kiwi': 3}
# Then, using a for loop, print the values of all the dictionary keys one by one.

# prices = {'apple': 2, 'kiwi': 3}
# for key in prices:
#     print(f"{key}: {prices[key]}")

# Create an empty set using the set() function and assign it to the numbers variable.
# Take an integer input from the user and assign it to the number variable.
# Add number to the numbers set using the set's add() method.
# Print the numbers set.
# number = set()
# num = int(input("Enter the number:"))
# number.add(num)
# print(number)


# Create a sequence of numbers 4, 7, 10 using the range() function.
# Convert this sequence to tuple using the tuple() function.
# Print the tuple.

# number = tuple(range(4, 11, 3))
# print(number)

# Create a program to find the greater common divisor of two numbers using the gcd() function defined inside the math module.

# Import the math module.
# Get two integer inputs from the user.
# Call the gcd() function with two numbers as arguments. The function returns the greatest common divisor.
# Print the result


# import math as m
# num1 = int(input("Enter the number:"))
# num2 = int(input("Enter the number:"))
# result = m.gcd(num1, num2)
# print(result)

# Take integer input from the user and store it in variable n.
# Create a nested loop. The outer loop should iterate n times.
# In each iteration of the outer loop, iterate the inner loop 2 times.
# Inside the inner loop, print '*'.


# n = int(input("Enter the no:"))
# for i in range(n):
#     for j in range(2):
#         print("*")

# To find the numbers between 50 to 100, we will need to create a loop that iterates from 50 to 100. In each iteration of the loop, we will check if the number is prime or not.

for i in range(50, 100, 1):
    prime = True
    for j in range(2, i, 1):
        if (i % j) == 0:
            prime = False
    if prime:
        print(i)
