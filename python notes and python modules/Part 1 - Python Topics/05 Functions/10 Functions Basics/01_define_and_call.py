# Example 1 (Easy): Define a function once, call it many times
# def = "define". The indented lines are the function body.


def greet():
    """Print a short welcome message."""        # a docstring explains what the function does
    print("Hello!")
    print("Welcome to Python functions.")


def line():
    print("-" * 30)


# Defining does NOT run the code. Calling (with parentheses) does.
greet()
greet()

line()
print("REPORT")
line()

# A function must be defined BEFORE the line that calls it
print(greet.__doc__)
