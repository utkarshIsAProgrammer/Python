# Making a set
fruits = {"pineapple", "guava", "guava", "banana", "mango"}
print(fruits, type(fruits))

# Length of set
print(len(fruits))

# Access set element
for fruit in fruits:
    print(fruit)

# Add element to set
fruits.add("orange")
print(fruits)

# Add set to a set
new_set = {"coconut", "dates", "almonds"}
fruits.update(new_set)
print(fruits)

# Remove set element
fruits.remove("coconut")  # error if the element not found
print(fruits)

fruits.discard("coconut")  # no error if the element not found
print(fruits)

# union() method
union_set = fruits.union(new_set)
print(union_set)

# same result as union
union_set = fruits | new_set
print(union_set)

# intersection() method
intersection_set = fruits.intersection(new_set)
print(intersection_set)

# same result as intersection
intersection_set = fruits & new_set
print(intersection_set)

# difference method
difference_set = fruits.difference(new_set)
print(difference_set)

# same result as difference
difference_set = fruits - new_set
print(difference_set)

# symmetric_difference() method
symmetric_difference = fruits.symmetric_difference(new_set)
print(symmetric_difference)

# same result as symmetric_difference
symmetric_difference = fruits ^ new_set
print(symmetric_difference)
