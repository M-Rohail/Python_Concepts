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


class Person:
    def __init__(self, name, age):
        self.current_name = name
        self.current_age = age


Person1 = Person("Phil", 19)
print(Person1.current_name)
print(Person1.current_age)
