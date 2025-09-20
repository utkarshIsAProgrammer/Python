# Quotes inside quotes
print("'Hello World!'")
print('"Hello World!"')

# Multiline string
multiline_string = """
This is a
multiline
string.
"""
print(multiline_string)

# String indexing
language = "Python"
print(language[0])
print(language[1])
print(language[-1])

# String length
print(len(language))

# Check string
print("n" in language)
print("N" in language)

print("n" not in language)
print("N" not in language)

# String slicing
print(language[:])
print(language[4:])
print(language[2:5])
print(language[-4:-1])
print(language[::2])

# Uppercase
print(language.upper())

# Lowercase
print(language.lower())

# Remove whitespace
a = "   Python   "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# Replace string
print(language.replace("P", "C"))

# Split string
print(a.split(" "))

# F string
print(f"{language} is my first programming language.")

# Placeholders and modifiers
print(f"My CGPA is {9:.2f}%")
print(f"My CGPA is {9.6298:.2f}%")
