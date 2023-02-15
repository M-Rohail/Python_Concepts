# Create a class named Triangle that will have three attributes x, y, z.
# Use the __init__() method to initialize attributes.
# Create a method named get_perimeter() to compute the perimeter and return it.
# Outside of the class

# Take three integer inputs and assign them to a, b and c respectively. These are the sides of a triangle.
# Create an object of the Triangle class with these values.
# Call the get_perimeter() method using the object which returns the perimeter.
# Print the perimeter
class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_perimeter(self):
        perimeter = self.x+self.y+self.z
        return perimeter


a = int(input("Enter the no:"))
b = int(input("Enter the no:"))
c = int(input("Enter the no:"))
tri = Triangle(a, b, c)
print(tri.get_perimeter())
