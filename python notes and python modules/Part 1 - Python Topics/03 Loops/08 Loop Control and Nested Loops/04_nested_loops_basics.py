# Example 4 (Intermediate): Nested loops - a loop inside a loop
# The inner loop runs COMPLETELY for each single step of the outer loop.

for row in range(1, 4):
    for col in range(1, 4):
        print(f"row {row}, col {col}")
    print("--- end of row", row, "---")

# Total steps = outer x inner
steps = 0
for i in range(4):
    for j in range(5):
        steps += 1
print("4 x 5 =", steps, "steps")

# Multiplication table 1 to 9
print("\nMultiplication table:")
for row in range(1, 10):
    for col in range(1, 10):
        print(f"{row * col:>3}", end=" ")
    print()
