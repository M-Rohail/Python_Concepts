# Create a class named Square that has an attribute named length.
# Use __init__() to initialize the length attribute.
# Create the compute_area() method to compute the area of a square and return it.
# Create the compute_perimter() method to compute the perimeter of a square and return it.
# Outside the class

# Take integer input from the user and store it in the length variable.
# Create an object of the Square class by passing length as an argument.
# Call the compute_area() method and print the area.
# Call the compute_perimeter() method and print the perimeter.
# By the way, the area of a square is equal to length * length, and the perimeter of a square is equal to 4 * length.

class square:
    def __init__(self, length):
        self.length = length

    def compute_area(self):
        area = self.length**2
        return area

    def compute_perimeter(self):
        perimeter = 4*self.length
        return perimeter


lengt = int(input("Enter yhe no:"))
sq = square(lengt)
print(sq.compute_area())
print(sq.compute_perimeter())
