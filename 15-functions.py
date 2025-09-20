# Defining and calling function
def greet(name):
    print(f"Hello, {name}!")


greet("Panchajanya")


# Function arguments
def info(name, age=25):
    print(f"{name} is {age} years old.")


info("Bob")
info("Carol", age=30)


# Returning values
def add(a, b):
    return a + b


result = add(5, 3)
print(result)

# Lambda(anonymous) function
square = lambda x: x * x
print(square(6))


# Function annotation
def divide(x: float, y: float) -> float:
    return x / y


print(divide(10, 2))


# Docstring
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


print(multiply(5, 6))
print(multiply.__doc__)


# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Scope
x = 10  # Global variable


def test_scope():
    x = 5  # Local variable
    print("Inside function:", x)


test_scope()
print("Outside function:", x)


# **args and **kwargs
def display_args(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)


display_args(1, 2, 3, name="Dave", age=40)


# Decorator
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@decorator
def say_hello():
    print("Hello!")


say_hello()
