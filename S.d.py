# Write a program to find standard deviation using the stdev() function of the statistics module.

# Import the statistics module.
# Create a list of data 2, 4, 6, 8, 10 and assign it to data_set variable.
# Print the standard deviation of data_set using stdev().
import statistics as s
data_set = [2, 4, 6, 8, 10]
sd = s.stdev(data_set)
print(sd)
