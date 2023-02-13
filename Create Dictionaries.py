# Write a program that uses a loop to take 3 key-value inputs from the user and create a dictionary using these keys and values.
# Create an empty dictionary named my_dict.
# Use for loop to iterate from 1 to 3, including 3.
# Inside the loop, take inputs for key and value and store them in my_dict.
# Print the updated my_dict.
# my_dict = {}
# i = 1
# while i < 4:
#     key = input("Enter the Key:")
#     val = input("Enter the value:")
#     if key == 4:
#         break
#     my_dict[key] = val
#     i = i+1
# print(my_dict)

# Write a program to print all values of a dictionary using a for loop.

# Create a dictionary named my_dict with keys and values "Elvis": 84, "Nelson": 74.
# Use for loop to iterate through my_dict.
# Inside the loop, print only values of respective keys.
# my_dict = {"Elvis": 84, "Nelson": 74}
# for i in my_dict:
#     print(my_dict[i])

# Write a program that checks if a value (entered by the user) is in a dictionary or not.
# Create a dictionary named my_dict with keys and values {"a": "juice", "b": "grill", "c": "corn"}.
# Take a string user input for the data variable.
# Create a flag variable and set it to False.
# Use a for loop to iterate through my_dict.
# Inside the loop, check if the value entered by the user is in the dictionary or not.
# If yes, set flag to True and terminate the loop.
# Outside the loop, if flag is equal to True, print "Value found" else print "Value not found".

my_dict = {"a": "juice", "b": "grill", "c": "corn"}
user = input("Enter the string:")
flag = False
for i in my_dict:
    if user == my_dict[i]:
        flag = True
        break
if flag:
    print("Value found")
else:
    print("Value not found")
