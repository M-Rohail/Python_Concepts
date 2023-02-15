# Create a class named Coordinate with attributes x and y.
# Use the __init__() method with two arguments to initialize these attributes.
# The class must also have a method named add_coordinates() that adds x and y attributes of two objects, then creates a new Coordinate object with these values, and returns the new Coordinate object.
# Outside the class

# Create two coordinates (objects of the Coordinate class) named c1 and c2.
# The x and y attributes of c1 should be 5 and 6 respectively.
# The x and y attributes of c2 should be 7 and 9 respectively.
# Call add_coordinates() using the c1 object with c2 as an argument, and store the result to the c3 variable.
# Print the x attribute of c3.
# Print the y attribute of c3.
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_coordinates(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Coordinate(new_x, new_y)


c1 = Coordinate(5, 6)
c2 = Coordinate(7, 9)
c3 = c1.add_coordinates(c2)
print(c3.x)
print(c3.y)
