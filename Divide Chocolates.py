# Create a program to divide N chocolates among M children.

# Get an integer value for the number of chocolates and assign it to the chocolates variable.
# Get an integer input for the number of children and assign it to the children variable.
# Find the number of chocolate each child gets after division and print it.
# Find the number of remaining chocolates and print it.
# Assumption: The number of chocolates will always be greater than the number of children.

chocolates = int(input("Enter the no:"))
children = int(input("Enter the no of childrens:"))
each = int(chocolates/children)
remaining = chocolates % children
print(each)
print(remaining)
