# Write a program to merge two dictionaries.

# Create a dictionary A with items {12: 'Kathmandu', 11: 'London', 3: 'Sydney'}.
# Create another dictionary B with items {10: 'New York', 2: 'Delhi'}.
# Merge these two dictionaries using update() and print it.

a = {12: "Kathmandu", 11: "London", 3: "Sydney"}
B = {10: "New York", 2: "delhi"}
a.update((B))
print(a)
