# Create a function

# Create a function named call_me() that takes two arguments a and b.
# Give default value 5 to argument a and 10 to argument b.
# Inside the function, print a and b in two separate lines.
# Outside of the function

# Take integer input and assign it to variable n.
# Call the call_me() function with n as an argument.

def call_me(a=5, b=10):
    print(a)
    print(b)


n = int(input("Enter the no :"))
call_me(n)
