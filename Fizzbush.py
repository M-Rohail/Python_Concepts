# Write a program to print FizzBuzz based on user input.

# Get an integer input from the user.
# If the number is multiple of 3, print "Fizz".
# If the number is multiple of 5, print "Buzz".
# If the number is multiple of both 3 and 5, print "FizzBuzz".
# Else print the original number.
User = int(input("Enter the no:"))
if User % 3 == 0 and User % 5 == 0:
    print("FizzBuzz")
elif User % 3 == 0:
    print("Fizz")
elif User % 5 == 0:
    print("Buzz")

else:
    print(User)
