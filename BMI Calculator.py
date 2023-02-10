# Create a program to find the BMI of a person.

# The formula to compute the BMI of a person is:

# BMI = weight / height**2
# Take a float input for the weight of a person (in kg) and assign it to the weight variable.
# Take a float type input for the height of the person (in meter) and assign it to the height variable.
# Use the formula to calculate the BMI.
# Print the BMI of the person.
weight = float(input("Enter your weight :"))
height = float(input("Enter the height :"))
BMI = float(weight/height**2)
print(BMI)
