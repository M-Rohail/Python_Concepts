# Create a program to find the cube of a number using a lambda function.

# Create the lambda function and assign it to a variable named num_cube.
# Take one integer input and assign it to number.
# Call the lambda function with number as argument and print the result.
def num_cube(x): return x**3


num = int(input("Enter the no:"))
result = num_cube(num)
print(result)
