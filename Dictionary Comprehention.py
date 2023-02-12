# Create a dictionary using dictionary comprehension.

# Take an integer input from the user and store it in variable n.
# Create a dictionary with keys from 1 to n. The value of the key must be 10 times the value of the key.
# Also, add a condition to the dictionary comprehension so that the key must be greater than or equal to 3.
# Print the dictionary.

n = int(input("Enter the no :"))
dic = {num: num*10 for num in range(1, n+1) if num >= 3}
print(dic)
