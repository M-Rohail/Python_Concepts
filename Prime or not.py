# Write a program to check whether a number is prime or not.

# A prime number is a number that is only divisible by either 1 or itself. For example, 7, 5, 19, etc.

# Problem Descriptions
# Get an integer input for the number variable.
# Run a loop from 2 to number, not including number, and check if number is divisible by any number between 2 to number - 1.
# If the number is divisible, print Not a Prime Number. Otherwise, print Prime Number.
prime = True
number = int(input("Enter the number:"))
for i in range(2, number):

    if number % i == 0:
        prime = False

if prime == True:
    print("Prime Number.")
else:
    print("Not a Prime Number.")
