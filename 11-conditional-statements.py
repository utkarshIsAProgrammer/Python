age = int(input("Enter you age: "))

# Conditional block
if age <= 0 or age >= 120:
    print("Don't be silly enter a valid age.")
elif age >= 18:
    print("You can watch this movie.")
else:
    print("You are not mature enough to watch this content.")

# Shorthand if-else
print(
    "Don't be silly enter a valid age."
    if age <= 0 or age >= 120
    else (
        "You can watch this movie."
        if age >= 18
        else "You are not mature enough to watch this content."
    )
)

# pass statement
if age < 18:
    pass
else:
    print("WOW! you are 18+ now.")
