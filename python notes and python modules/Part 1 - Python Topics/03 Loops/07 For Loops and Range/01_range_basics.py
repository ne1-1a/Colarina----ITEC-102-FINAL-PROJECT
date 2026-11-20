# Example 1 (Easy): for + range() - repeat a known number of times
# range(stop)  ->  0, 1, 2, ... stop-1   (stop is NOT included)
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()

# range(start, stop, step)
print("range(2, 11, 2):")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Repeat something N times (the variable name can be _ when you do not use it)
for _ in range(3):
    print("Hello!")

# The loop variable can have any name
for day in range(1, 4):
    print("Day", day)
