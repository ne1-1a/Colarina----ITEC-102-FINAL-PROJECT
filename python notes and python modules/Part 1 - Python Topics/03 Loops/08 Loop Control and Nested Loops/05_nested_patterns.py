# Example 5 (Intermediate): Drawing patterns with nested loops

print("Rectangle (4 rows x 8 columns):")
for row in range(4):
    for col in range(8):
        print("#", end="")
    print()

print("\nHollow rectangle:")
for row in range(5):
    for col in range(8):
        if row == 0 or row == 4 or col == 0 or col == 7:
            print("#", end="")
        else:
            print(" ", end="")
    print()

print("\nNumber triangle:")
for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

print("\nCheckerboard:")
for row in range(4):
    for col in range(8):
        if (row + col) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()
