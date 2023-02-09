# Create a program to print a sentence.

# Print Python is interesting on the screen.

# print("Python is interesting on the screen.")


# Create a program to print a sentence and an integer.

# Print Python is interesting on the first line.
# Print 75 on the next line.
# print("Python is interesting.")
# print(75)


# Create a program to print a variable.
# Create a variable named salary and assign 4950.5 to it.
# Print the variable.

# salary = 4950.5
# print(salary)

# Create a program to change the value of a variable
# Declare a variable named country.
# Assign string 'United States' to it.
# Print the variable.
# Change the value of the variable to 'Canada'.
# Print the variable again.

# country = "United States"
# print(country)
# country = "Canada"
# print(country)

# Create a program to assign one variable to another.

# Create a variable named favorite_food with the value 'steak'.
# Print the favorite_food variable.
# Create another variable named food with the value 'pizza'.
# Assign the food variable to the favorite_food variable.
# Print the favorite_food variable again.

# favorite_food = 'steak'
# print(favorite_food)
# food = 'Pizza'
# favorite_food = food
# print(favorite_food)


# Create a program to find profit and print it.

# Suppose the cost price of a book is 25 dollars. Store it in a variable named cost_price.
# The selling price of the book is 35 dollars. Store it in a variable named selling_price.
# Calculate the profit amount on the book

# cost_price = 25
# selling_price = 35
# profit_amount = selling_price-cost_price
# print("Profit_amount:", profit_amount)

# Create a program to divide pens among students.

# Suppose you have to divide 14 pens among 3 students equally.
# You need to find out how many pens each student would get (if pens must be divided equally), and the number of remaining pens that cannot be divided.
# To solve this problem, create a variable named pens_number and assign 14 to it.
# Create another variable named students_number and assign 3 to it.
# Compute the number of pens each student will get and print it.
# Compute the number of remaining pens and print it.
# pens_number = 14
# no_of_students = 3
# each_student = pens_number//no_of_students
# remaining_pen = pens_number % no_of_students
# print(each_student)
# print(remaining_pen)


# Suppose you are a university student and you need to pay 1536 dollars as a tuition fee.

# The college is offering a 10% discount on an early payment. How much money do you have to pay if you make the early payment?

# Task

# Create a variable named fee and assign 1536 to it.
# Create another variable discount_percent and assign 10 to it.
# Compute discount by using formula discount_percent/100 *fee and assign it to the discount variable.
# Compute and print the fee you have to pay by subtracting discount from fee.

# fee = 1536
# discount_percentage = 10
# discount = discount_percentage/100*fee
# pay = fee-discount
# print("You have to pay:", pay)
# print(discount)


# Create a program to convert a variable of one type to another.

# Create a variable named x and assign a string value '5' to it.
# Create another variable y and assign '10' to it.
# Convert the value stored in x and y to integers and multiply them.
# Print the result.

# x = "5"
# y = '10'
# print(int(x)*int(y))

# Ask the user to enter the first name and store it in the first_name variable.
# Ask the user to enter the second name and store it in the second_name variable.
# Print the full name.
# first_name = input("Enter your first name: ")
# second_name = input("Enter your second name: ")

# print("Full name:", first_name + " " + second_name)

# Create a program to perform arithmetic operations on user input.

# Get two numeric type input from the user, convert them to float and assign them to variables number1 and number2.
# Add number1 and number2, and store the result in the result variable.
# Then, print the square of the result variable.

# number_1 = float(input("Enter The Number :"))
# number_2 = float(input("Enter the number :"))
# result = number_1+number_2
# print(result**2)

# Create a program to convert temperature from celsius to fahrenheit.

# Formula:

# fahrenheit = (celsius * 1.8) + 32
# Get temperature in Celsius from the user and assign it to a variable.
# Convert it to degree Fahrenheit using the above formula.
# Print the result.
# temperature_Celcius = float(input("Enter the temperature in celcius:"))
# temperature_fahrenheit = (temperature_Celcius*1.8)+32
# print(temperature_fahrenheit)

# Area of a Triangle
# If a, b and c are three sides of a triangle. Then,

# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# Problem Description
# Get three numeric inputs from the user and store them in variables a, b and c.
# Compute semiperimeter s and then the area of the triangle using the above formula.
# Print the area.
# a = float(input("Enter the number: "))
# b = float(input("Enter the number: "))
# c = float(input("Enter the number: "))
# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print(area)


# Program to print True if the number is divisible by 5. If not, print False.

# Get an integer input from the user.
# Check if the input is divisible by 5 or not. If it's divisible by 5, print True. If not, print False.
# integer = int(input("Enter a number:"))
# print(integer % 5 == 0)


# Take three integer inputs from the user and store them in n1, n2, and n3 respectively.

# If n3 is the smallest number, print True.
# If n3 is not the smallest number, print False.

# n1 = int(input("Enter the number:"))
# n2 = int(input("Enter the number:"))
# n3 = int(input("Enter the number:"))
# print(n3 < n1 and n3 < n2)

# Check whether a person can vote or not depending upon his/her age.

# Get integer input from the user and store it in the age variable.
# If age is 18 or above, print The person can vote.. If not, don't print anything.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")

# Check whether a person can vote or not depending upon his/her age.

# Get integer input from the user and store it in the age variable.
# If age is 18 or above, print The person can vote.. If not, print The person cannot vote..
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("The person can vote.")
# else:
#     print("The person cannot vote.")

# Create a program to check whether a number is positive or negative or zero.

# Get integer input from the user and store it in the number variable.
# If number is positive, print positive.
# If number is negative, print negative.
# If number is 0, print zero.
# num = int(input("Enter the number :"))
# if num > 0:
#     print("positive.")
# elif num < 0:
#     print("negative.")
# else:
#     print("zero.")

# Create a program to check whether a number is even or odd.

# Get integer input from the user and store it in the number variable.
# If number is even, print even.
# If number is odd, print odd.
# Hint: A number is even if the remainder is 0 when it's divided by 2. Basically, if number % 2 is equal to 0, the number is even.
# num = int(input("Enter the number:"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# Create a program to print numbers from 5 to 1 using a while loop.

# Create variable i with value 5.
# Inside a while loop, print the value of i.
# Decrease the value of i by 1 in each iteration of the loop.

# i = 5
# while i > 0:
#     print(i)
#     i = i-1

# Create a program to find the factorial of an integer entered by the user.

# The factorial of a positive integer n is equal to 1 * 2 * 3 * ... * n. For example, the factorial of 4 is 1 * 2 * 3 * 4 which is 24.

# Take an integer input from the user and assign it to the variable n. We will assume the user will always enter a positive integer.
# Create a variable named total to store the result.
# Create a temporary variable i with initial value 1.
# Run a while loop until the value of i becomes greater than n.
# Inside the loop multiply the value of i and total and assign the result to total.
# Increase the value of i.
# Outside the loop, print the value of total.
# n = int(input("Enter the number :"))
# total = 1
# i = 1
# while n >= i:
#     total = total*n
#     n = n-1

# print("Factorial :", total)

# Create a program to print individual characters of a string using a for loop.

# Get string input from the user and store it in a variable.
# Using a for loop, print its individual characters.
# line = input("Enter the line :")
# for var in line:
#     print(var)

# print sum of natural number
# num = int(input("Enter the number:"))
# total = 0
# for i in range(1, num+1):
#     total = total+i

# print(total)

# Create a program to find the factorial of an integer entered by the user.

# The factorial of a positive integer n is equal to 1 * 2 * 3 * ... * n. For example, the factorial of 4 is 1 * 2 * 3 * 4 which is 24.

# Take an integer input from the user and assign it to the variable n. We will assume the user will always enter a positive integer.
# Using a for loop, compute the factorial.
# Print the factorial at the end.


# n = int(input("Enter the number:"))
# total = 1
# for i in range(1, n+1):
#     total = total*i

# print(total)


# Create a program to print odd numbers between 1 and n (entered by the user).

# Get an integer input from the user. We will assume the user will enter a positive integer.
# Using a loop, iterate from 1 to n (n should be inclusive).
# In each iteration of the loop, print the number if it's an odd number.
# n = int(input("Enter the number:"))
# for i in range(1, n+1):
#     if i % 2 == 1:
#         print("i")


# total = 0

# while True:
#     total = total+n
#     n = int(input("Enter the number:"))
#     if n == 0:
#         break
# print("Outside")
# print(total)

# Create a program to calculate the sum of integers entered by the user. If the user enters 0 or negative integer, terminate the loop and print the sum.

# Initialize a variable named total with value 0 at the beginning.
# Create a while loop with condition True.
# If the user enters 0 or negative integer, use break to terminate the loop.
# If the user enters a positive number, add it to the total variable.
# Print the total from outside of the loop.
# total = 0
# while True:
#     n = int(input("Enter the number:"))
#     if n == 0 or n < 0:
#         break
#     elif n > 0:
#         total = total+n

# print(total)

# Create a program to print odd numbers between 1 and n, where n is a positive integer entered by the user.

# Take integer input from the user and store it in variable n.
# Use a for loop to iterate from number equal to 1 to n+1.
# If number is even, use continue to skip the number from printing.
# If number is odd, print the number.
# n = int(input("Enter the number:"))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# Create a program to find the multiplication table of an integer (entered by the user) from 6 to 9.

# Take integer input and store it in variable n.
# Using a for loop, find the multiplication table of n from 6 to 9 in the specified format below.
# n = int(input("Enter the number:"))
# for i in range(6, 10):
#     print(n, "times", i, "is", n*i)

# Create a program to continuously ask integer input from the number using an infinite while loop.

# If the number is between 1 and 100 (inclusive), print the number.

# However, if the number is outside of this range, terminate the loop.

# while True:
#     n = int(input("Enter the no:"))
#     if n > 0 and n < 101:
#         print(n)
#         continue
#     else:
#         break

# Create a function named print_numbers().

# Inside the function, put two print statements:

# print(5)
# print(100)
# Call the print_numbers() function two times.
# def print_number():
#     print(5)
#     print(100)


# print_number()
# print_number()

# Create a function to print a person's information.

# Step 1

# Create a function named display_info().
# This function must accept two arguments: name and location.
# Print name and location in two separate lines.
# Step 2

# Outside of the function:

# Get string input from the user and assign it to the country variable.
# Call the display_info() with arguments: the 'Taylor' string and the country variable, respectively.
# For more hints, see the code outline.

# def display_info(name, location):
#     print(name)
#     print(location)


# country = input("Enter your country name:")
# display_info("Taylor", country)


# Create a function to find the product of two numbers.

# Step 1

# Create a function:

# Create a function named get_product().
# This function should accept two arguments: number1 and number2.
# Multiply number1 and number2 and return the result.
# Step 2

# Outside of the function:

# Get two integer inputs from the user and store them in n1 and n2.
# Call the get_product() function with arguments n1 and n2 respectively and store the value returned in the total variable.
# Print the total.
# For more hints, see the code outline.
# def get_product(number1, number2):
#     result = number1*number2
#     return result


# n1 = int(input("Enter the number:"))
# n2 = int(input("Enter the number:"))
# total = get_product(n1, n2)
# print(total)

# Create a function to compute the factorial of a number. The factorial of a positive integer n is equal to:

# factorial = 1 * 2 * 3 * ... * n
# Step 1

# Create a function named compute_factorial().
# This function takes only one argument, n, and computes the factorial.
# Return the factorial.
# Step 2

# Outside of the function:

# Get an integer input from the user and store it in the number variable.
# Call the compute_factorial() with number as an argument, and assign the returned value to the total variable.
# Print the total variable.
# def compute_factorial(n):
#     total = 1
#     for i in range(1, n+1):
#         total = total*i

#     return total


# number = int(input("Enter the number:"))
# total = compute_factorial(number)
# print(total)
