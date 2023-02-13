# Create a class

# Create a class named Person.
# Inside this class, create a method named greet() that takes two arguments: self and message.
# Print message from inside the greet() method.
# Outside of the class

# Get string input from the user and assign it to the greeting variable.
# Create an object named person1 of the Person class.
# Call the greet() method using the person1 object with greeting as an argument.

# class Person:
#     def greet(self, message):
#         print(message)


# greeting = input("Enter :")
# person1 = Person()
# person1.greet(greeting)

# Create a class

# Create a class named Person.
# Inside this class, create the __init__() method that takes three arguments: self and name and age.
# Inside the __init__() method, create two attributes named current_name and current_age. Then, assign the name argument to the current_name attribute, and the age argument to the current_age attribute.
# Outside of the class

# Create an object named person1 of the Person class. While creating this object, use 'Phil' as the first argument and 19 as the second argument.
# Print the current_name attribute of the person1 object.
# Print the current_age attribute of the person1 object.


# class Person:
#     def __init__(self, name, age):
#         self.current_name = name
#         self.current_age = age


# Person1 = Person("Phil", 19)
# print(Person1.current_name)
# print(Person1.current_age)

# Create a class

# Create a class named Triangle.
# Create the __init__() method that takes four arguments self, a, b and c. The a, b and c arguments represent sides of a triangle.
# Inside the __init__() method, create three attributes s1, s2 and s3 and assign values a, b and c to the attributes.
# Create a method named get_perimeter() to compute perimeter and return it. If you don't know, the perimeter is equal to the sum of the sides.
# Outside of the class
# Take three integer inputs from the user to represent the sides of a triangle.
# Create an object of the Triangle class using the given inputs.
# Call the get_perimeter() method using the object and print the perimeter.
class Triangle:
    def __init__(self, a, b, c):
        self.s1 = a
        self.s2 = b
        self.s3 = c

    def get_perimeter(self):
        perimeter = self.s1+self.s2+self.s3
        return perimeter


a = int(input("Enter:"))
b = int(input("Enter:"))
c = int(input("Enter:"))
Tri = Triangle(a, b, c)
print(Tri.get_perimeter())
