# Create a program to print the item present at a given index. If the index is out of bounds, print Wrong index.

# Create a list of four strings: 'BMW', 'Ferrari', 'Audi', 'Tesla'.
# Take an integer input from the user and store it in the index variable.
# Print the item present at that index.
# However, if the index is out of bounds, instead of showing the default error, print Wrong Index.
# Note: Use exception handling to solve this problem.
car_brands = ['BMW', 'Ferrari', 'Audi', 'Tesla']

try:
    index = int(input("Enter an index: "))
    print(car_brands[index])
except IndexError:
    print("Wrong Index")
