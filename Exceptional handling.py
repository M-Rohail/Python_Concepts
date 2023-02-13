# Create a program to print an item of a list based on user input (index). If the index doesn't exist in a list, print a custom message.

# Assign a list, [10, 20, 30], to the numbers variable.
# Take an integer input and assign it to the index variable.
# Print the item at that given index.
# However, if the index is not in the list, print a custom message 'Index is wrong'.
# Use exception handling to solve this problem.
# numbers = [10, 20, 30]
# temp = True
# index = int(input("Enter the no:"))
# try:
#     for i in numbers:
#         if index == i:
#             temp = True
#             break
# except:
#     temp = False

# if temp:
#     print(index)
# else:
#     print("Index is wrong")
# numbers = [10, 20, 30]
# length = len(numbers)
# try:
#     index = int(input("Enter the index of the item you want to access: "))

#     if length <= index:
#         print(numbers[index])

# except:
#     print("Index is wrong.")

numbers = [10, 20, 30]
length = len(numbers)

try:
    index = int(input("Enter the index of the item you want to access: "))

    if index >= 0 and index < length:
        print(numbers[index])
    else:
        print("Index is wrong")
except IndexError:
    print("Index is wrong")
