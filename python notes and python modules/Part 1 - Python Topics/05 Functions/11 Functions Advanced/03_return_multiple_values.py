# Example 3 (Intermediate): Returning more than one value
# Python packs the values together; you unpack them into separate variables.


def min_max(a, b, c):
    smallest = a
    largest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return smallest, largest


low, high = min_max(7, 2, 9)
print("Smallest:", low, "| Largest:", high)


def divide_with_remainder(a, b):
    return a // b, a % b


quotient, remainder = divide_with_remainder(17, 5)
print(f"17 / 5 = {quotient} remainder {remainder}")

# If you do not unpack, you get ONE packed value
packed = divide_with_remainder(17, 5)
print("Packed result:", packed)

# Use _ for a value you do not need
_, only_remainder = divide_with_remainder(100, 7)
print("Only the remainder:", only_remainder)


def circle_info(radius):
    area = 3.14159 * radius ** 2
    circumference = 2 * 3.14159 * radius
    return area, circumference


area, circumference = circle_info(5)
print(f"Area {area:.2f}, circumference {circumference:.2f}")


# A very common pattern: return (success?, message)
def check_age(age):
    if age < 0:
        return False, "Age cannot be negative"
    if age < 18:
        return False, "You must be 18 or older"
    return True, "Welcome!"


def show_check(age):
    ok, message = check_age(age)
    print(f"Age {age}: {ok} - {message}")


show_check(-1)
show_check(15)
show_check(20)
