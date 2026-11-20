# Example 2 (Easy-Intermediate): Steps, negative steps and empty ranges

# Positive step: count by tens
for i in range(0, 50, 10):
    print(i, end=" ")
print()

# Negative step: count DOWN (start must be bigger than stop)
for i in range(10, 0, -1):
    print(i, end=" ")
print("Liftoff!")

for i in range(10, 0, -3):
    print(i, end=" ")
print()

# Negative numbers work too
for i in range(-3, 4):
    print(i, end=" ")
print()

# An impossible range is simply empty (no error)
for i in range(5, 1):
    print("This never prints")
print("range(5, 1) gave nothing because the step is +1 and 5 is already past 1")

# How many numbers does a range produce? Count them.
count = 0
for _ in range(3, 20, 4):      # 3, 7, 11, 15, 19
    count += 1
print("range(3, 20, 4) produces", count, "numbers")
