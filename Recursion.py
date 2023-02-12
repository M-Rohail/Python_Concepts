# Create a program to find the factorial of a number using recursion.

# Take a positive integer input
# Find the factorial by creating a recursive function.
# We will assume the user will also enter a positive integer.

def fac(n):
    if n != 1:
        n = n * fac(n-1)
    return n


val = int(input("Enter the no:"))
factorial = fac(val)
print(factorial)
