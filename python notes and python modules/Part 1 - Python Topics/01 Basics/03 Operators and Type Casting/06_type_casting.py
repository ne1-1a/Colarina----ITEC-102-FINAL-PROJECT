# Example 6 (Intermediate): Type casting - converting between types
print(int("42") + 8)                # text -> int
print(float("3.5") * 2)             # text -> float
print(str(100) + " points")         # number -> text

# int() CUTS OFF decimals, round() rounds
print(int(9.99))                    # 9
print(round(9.99))                  # 10
print(int(-2.7))                    # -2 (cuts toward zero)

print(float(7))                     # 7.0
print(int(True), int(False))        # 1 0

# int("3.5") would crash. Go through float first:
print(int(float("3.5")))

# Build a sentence from numbers
age = 19
print("I am " + str(age) + " years old")

# bool() of text and numbers
print(bool(""), bool("hello"), bool(0), bool(7))
