# Example 2 (Easy-Intermediate): Parameters - give a function information
# parameter = the name in the def line | argument = the value you pass when calling


def greet(name):
    print(f"Hello, {name}!")


greet("Alex")
greet("Sam")


def add(a, b):
    print(f"{a} + {b} = {a + b}")


add(3, 4)
add(10, 25)


def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


introduce("Alex", 19, "Manila")             # positional: ORDER matters
introduce(age=19, city="Manila", name="Alex")   # keyword: order does not matter


def repeat_text(text, times):
    print(text * times)


repeat_text("Ha", 3)
repeat_text("-=", 10)
