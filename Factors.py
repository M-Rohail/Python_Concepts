# Write a program to print all factors of a number.

# Get an integer input and assign it to the number variable.
# Create a for loop that iterates from 1 to number.
# Inside the loop, check if number is perfectly divisible by i (remainder 0).
# If so, print the value of i.

number = int(input("Enter the number :"))
for i in range(1, number+1):
    if number % i == 0:
        print(i)
