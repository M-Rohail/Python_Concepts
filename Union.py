# Write a program to get the union of two sets.
# Create a set named developers with elements "Mark", "George", "Ben".
# Create another set named designers with elements "Andy", "Jared", "Ben".
# Use the union() function to return a new set with distinct elements from all the sets.
# Print the new set that contains all elements of developers and designers set.

developers = {"Mark", "George", "Ben"}
designers = {"Andy", "Jared", "Ben"}
new = {}
new = developers.union(designers)
print(new)
