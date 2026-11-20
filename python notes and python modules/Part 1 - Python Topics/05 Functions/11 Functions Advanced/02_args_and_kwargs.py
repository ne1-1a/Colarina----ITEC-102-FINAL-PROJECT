# Example 2 (Intermediate): A flexible number of arguments

# *args collects ALL extra positional arguments (inside the function it acts like a group of values)
def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))
print(add_all())                    # zero arguments is fine


def average(*scores):
    if len(scores) == 0:
        return 0
    return add_all(*scores) / len(scores)       # the * also UNPACKS values when calling


print(average(80, 90, 100))
print(average())


def biggest(*numbers):
    best = None                      # None = "nothing yet"
    for n in numbers:
        if best is None or n > best:
            best = n
    return best


print(biggest(4, 19, 7, 12))


# Normal parameters first, then *args
def order_pizza(size, *toppings):
    print(f"A {size} pizza with:")
    for topping in toppings:
        print("  -", topping)


order_pizza("large", "cheese", "pepperoni", "mushroom")
order_pizza("small")


# BONUS: **kwargs collects extra KEYWORD arguments (it uses a dictionary inside;
# dictionaries belong to Data Structures, so this is only a taste)
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_profile(name="Alex", age=19, course="BSCS")
