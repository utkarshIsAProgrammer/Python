# Making list
fruits = ["pineapple", "mango", "orange", "banana", "guava"]
print(fruits, type(fruits))

# Length of list
print(len(fruits))

# list() constructor
new_list = list(["apple", "kiwi", "strawberry"])
print(new_list)

# Accessing list item
print(new_list[0])
print(new_list[1])
print(new_list[-1])

print(fruits[2:4])
print(fruits[-5:-3])
print(fruits[::2])

# Change element value
new_list[0] = "papaya"
print(new_list[0])

fruits[::2] = ["grapes", "raspberry", "litchi"]
print(fruits)

# Insert elements
new_list.insert(0, "apple")
print(new_list)

# Append elements
fruits.append("marshmallow")
print(fruits[-1])

# Extend list
fruits.extend(new_list)
print(fruits)

# Removing specified element
fruits.remove("litchi")
print(fruits)

# Removing specified index
fruits.pop(2)
print(fruits)

del fruits[3]
print(fruits)

# Removing last element
fruits.pop()
print(fruits)

# Clear the list
new_list.clear()
print(new_list)

# List comprehension
# Syntax = [Expression ForLoop Condition]
[print(fruit) for fruit in fruits if (fruits != [])]

# Sort list
# 1. Ascending order
fruits.sort()
print(fruits)

# 2. Descending order
fruits.sort(reverse=True)
print(fruits)

# 3. Reverse order
fruits.reverse()
print(fruits)

# Copy list
fruits_clone = fruits.copy()
print(fruits_clone)

# Join list
repeated_fruits = fruits + fruits_clone
print(repeated_fruits)
