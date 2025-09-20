# Making a dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "white"}
print(car, type(car))

# Dictionary length
print(len(car))

# Dictionary constructor
employee = dict({"name": "Panchajanya", "age": 19, "role": "Fullstack Developer"})
print(employee)

# Access items
print(employee.get("name"))
print(employee.get("age"))
print(employee["role"])

# Get keys of the dictionary
print(employee.keys())

# Get values of the dictionary
print(employee.values())

# Get all key-value paris of dictionary
print(employee.items())

# Change values
employee["age"] = 20
print(employee.get("age"))

# Update dictionary
employee.update({"experience": "6 months"})
print(employee.get("experience"))

# Add key-value pair to the dictionary
employee["name"] = "Utkarsh"
print(employee["name"])

# Remove specified item
car.pop("model")
print(car)

del car["year"]
print(car)

# Remove last inserted item
car.popitem()
print(car)

# Clear dictionary
car.clear()
print(car)

# Copy dictionary
duplicate_employee = employee.copy()
print(duplicate_employee)
