# Write a program to print fibonacci numbers.

# Hint: A Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers. For example,

# 1 1 2 3 5 8
# Task:

# Take integer input from the user and store it in n.
# Define two integer variables t1 and t2 both with the value of 1.
# Use a for loop to loop from i = 1 to n, including n.
# In each iteration, print the value of t1.
# Also, define the result variable as the sum of t1 and t2.
# Assign the value of t2 to t1.
# Assign the value of result to t2.

n = int(input("Enter the no:"))
t1 = 1
t2 = 1
for i in range(1, n+1):
    print(t1)
    result = t1+t2
    t1 = t2
    t2 = result
