# Write a program to find the power of a number using the math module.

# Import the math module.
# Get an integer input in variable num.
# Calculate the power of num raised to 4 using pow() function of math module.
# Print the result.


import math as m
num = int(input("Enter the no:"))
result = m.pow(num, 4)
print(result)
