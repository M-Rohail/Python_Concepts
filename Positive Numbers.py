# Write a program to print numbers until the user enters 0 or a negative number.

# Run a while loop that is always True.
# Inside the loop, get an integer input value from the user and store it in the number variable.
# Check if number is less than 0. If yes, skip the current iteration.
# Check if number is equal to 0. If yes, terminate the loop.
# If the user input is a positive number, print all the values of number.

while (True):
    number = int(input("Enter the no:"))
    if number < 0:
        continue
    elif number == 0:
        break
    elif number > 0:
        print(number)
