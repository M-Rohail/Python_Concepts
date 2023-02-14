# Create a program to find the sum of the square root of two numbers using a lambda function.

# Create the lambda function and assign it to a variable named compute.
# The function should take two arguments and return the sum of the square roots of the arguments.
# Take two integer inputs and assign them to n1 and n2 respectively.
# Call the lambda function with n1 and n2 as arguments and print the result.

def named(x, y): return x**0.5 + y**0.5


n1 = int(input("Enter the no:"))
n2 = int(input("Enter the no:"))
result = named(n1, n2)
print(result)
