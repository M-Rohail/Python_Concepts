# Create the Vehicle class

# Create a class named Vehicle.
# Inside this class, create a method named get_vehicle_features().
# Inside this method, print 'Initializing vehicle features'.
# Create the Car class

# Derive a class named Car from the Vehicle base class.
# Inside this class, create a method named get_car_features().
# In this method, print 'Initializing car features'.
# Outside of the classes

# Create an object of the Car class.
# Access the get_vehicle_features() method using the object.
# Then, access the get_car_features() method using the object.
# class Vehicle:
#     def get_vehicle_features(self):
#         print('Initializing vehicle features')


# class Car(Vehicle):
#     def get_car_features(self):
#         print('Initializing car features')


# c1 = Car()
# c1.get_vehicle_features()
# c1.get_car_features()


#  In this example, we will create a program to calculate the perimeter of different polygons like triangles and quadrilaterals using inheritance.

# We will first create a Polygon class that has the __init__() method. Inside this method, we will initialize the sides attribute.
# Inside the Polygon class, we will create two more methods: one to calculate perimeter and the other to display the info of the polygon.
# Then, we will derive a Triangle class and a Quadrilateral class from it and put methods specific to these classes inside it.

# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides

#     def perimeter(self):
#         peri = sum(self.sides)
#         return peri

#     def display(self):
#         print("This is a Polygon Class:")


# class Triangle(Polygon):
#     def display(self):
#         print("This is a triangle:")


# class Quadrilateral(Polygon):
#     def display(self):
#         print("A quadrilateral is a polygon with 4 edges.")
#         super().display()


# Q1 = Quadrilateral([2, 2, 2, 2])
# # Q1 = Quadrilateral([2, 2, 4, 4])
# # print("Perimeter of Quadrilateral :", Q1.perimeter())
# Q1.display()


# Starting from the Person class we created in the last example,

# Derive a class named Student from Person.
# Inside the Student class, create the __init__() method that takes self and student_id as arguments.
# Create an attribute named id and assign student_id to it, and then call the __init__() method of Person using super().
# Create another method named display_info() inside Student. Inside the method, call the display_info() method of Person using super(), and then print the id attribute.
# Outside of classes

# Create an object of Student with 12 as argument.
# Call the display_info() method using the object.
# For hints, see the code outline

class Person:
    def __init__(self):
        name = input("Enter your Name:")
        age = input("Enter Your Age:")
        self.name = name
        self.age = age

    def display_info(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")


class Student(Person):
    def __init__(self, student_id):
        self.id = student_id
        super().__init__()

    def display_info(self):
        super().display_info()
        print(f"id:{self.id}")


s1 = Student(12)
s1.display_info()
