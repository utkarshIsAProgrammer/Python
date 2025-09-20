# Making a tuple
fruits = ("pineapple", "banana", "mango", "guava")
print(fruits, type(fruits))

# One element tuple
disliked_fruit = ("apple",)
print(disliked_fruit, type(disliked_fruit))

# Tuple length
print(len(fruits))
print(len(disliked_fruit))

# Tuple constructor
this_tuple = tuple((1,))
print(this_tuple, type(this_tuple))

# Access tuple
print(fruits[0])
print(fruits[1])
print(fruits[-1])

print(fruits[1:3])
print(fruits[::2])
print(fruits[-3:-1])

# Check if item exists
print("pineapple" in fruits)

# Concatenation
print(fruits + this_tuple)

# Unpacking
a, b, c, d = fruits
print(a, b, c, d)

a, b, *c = fruits
print(a, b, c)

# Tuple multiplication
print(this_tuple * 5)
