# Create a program to calculate the simple interest and the final amount.

# Use the following formula to calculate the interest and final amount:

# Simple Interest = P * R * T * .01
# Final Amount = P + Simple Interest
# Here, P is the principal amount, R is the rate of interest and T is the time in years.

# Take float input for principal, rate and time, respectively.
# Calculate the simple interest using the formula and store the result in interest.
# Calculate the final amount using the formula and store it in total_sum.
# Print interest and total_sum in separate lines.

p = float(input("Enter the principal Amount:"))
r = float(input("Enter rhe value:"))
T = float(input("Enter The value"))
simple = p*r*T*0.1
final_amount = p+simple
print(simple)
print(final_amount)
