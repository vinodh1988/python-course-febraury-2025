# Demonstrating basic operations with sets in Python

# Creating a set
my_set = {1, 2, 3, 4, 5,6,6,6,6}
print("Original set:", my_set)

# Set is unordered and no indexing

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Checking if an element is in the set
print("Is 2 in the set?", 2 in my_set)

# Iterating through a set
print("Iterating through the set:")
for element in my_set:
    print(element)

# Set operations
another_set = {4, 5, 6, 7, 8}

# Union
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Symmetric Difference
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("Symmetric difference of sets:", symmetric_difference_set)
