# Example 4 (Intermediate): Combine conditions with and / or / not
age = int(input("Your age: "))
height_cm = int(input("Your height in cm: "))

# AND: both must be True
if age >= 12 and height_cm >= 140:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you are too young or too short.")

# OR: at least one must be True
if age < 5 or age > 65:
    print("Free entrance to the park.")
else:
    print("Regular entrance fee.")

# NOT: flips the answer
is_weekend = False
if not is_weekend:
    print("Park offers a weekday discount.")

# Keep conditions readable: use parentheses when mixing and / or
if (age >= 18 and height_cm >= 150) or age >= 60:
    print("You can join the adult tour.")
