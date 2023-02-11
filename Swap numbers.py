# Create a program to swap two integers entered by the user.

# Get two integer user inputs in variables n1 and n2.
# Swap the values of these two variables using a temporary variable temp.
# Print the values of n1 and n2.
n1 = int(input("Enter the no:"))
n2 = int(input("Enter the no:"))
temp = n1
n1 = n2
n2 = temp
print(n1)
print(n2)
