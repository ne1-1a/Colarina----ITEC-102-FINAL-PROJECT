# Example 8 (Hard) MINI PROJECT 3: Pattern printer (for + range + string multiplication)
height = int(input("Pattern height: "))

print("\nRight triangle:")
for i in range(1, height + 1):
    print("*" * i)

print("\nInverted triangle:")
for i in range(height, 0, -1):
    print("*" * i)

print("\nPyramid:")
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print("\nNumber triangle:")
for i in range(1, height + 1):
    print(str(i) * i)
