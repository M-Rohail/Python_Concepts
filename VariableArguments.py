# Write a program to create a function that can take a variable number of arguments and returns the product of numbers passed as arguments.

# Create a function named multiply_numbers() that can take any number of arguments (0 or more).
# Inside the function, calculate the product of numbers passed as arguments and return the result.
# Outside the function

# Take three integer inputs from the user.
# Call the multiply_numbers() function with these three integers and print the return value.

def multiply_numbers(*a):
    p = 1
    for i in a:
        p = p*i
    return p


n1 = int(input("Enter the no:"))

n2 = int(input("Enter the no:"))

n3 = int(input("Enter the no:"))
result = multiply_numbers(n1, n2, n3)
print(result)
