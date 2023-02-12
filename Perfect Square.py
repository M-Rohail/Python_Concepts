# Write a program to check if a number is a perfect square or not.

# Import math module.
# Get an integer input and store it in the number variable.
# Find the square root of the number using sqrt() function and assign it to square_root variable.
# Use the % operator with 1 to get the remainder of the calculated square root and assign it to check_remainder.
# If the remainder is equal to 0, print Perfect Square.
# Else print Not a Perfect Square.
import math
number = int(input("Enter the no:"))
square_root = math.sqrt(number)
remaider = square_root % 1
if remaider == 0:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
