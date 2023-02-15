# Create Classes

# Create two classes: Engine with attribute power, and Vehicle with attributes: wheels and engine.
# Use the __init__() method with two arguments: self and power to create and initialize the power attribute of the Engine class.
# Use the __init__() method with two arguments self and wheels to initialize the wheels attribute of the Vehicle class.
# Inside the __init__() method of Vehicle, the engine attribute should be assigned with an object of the Engine class with the power attribute equal to 400.
# Create another method named get_power() inside the Vehicle class and print the power attribute of the engine attribute.
# Outside classes

# Create an object of the Vehicle class with wheels attribute equal to 4.
# Call the get_power() method of this object.

class Engine:
    def __init__(self, power):
        self.power = power


class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
        self.engine = Engine(power=400)

    def get_power(self):
        print(self.engine.power)


s2 = Vehicle(wheels=4)
s2.get_power()
