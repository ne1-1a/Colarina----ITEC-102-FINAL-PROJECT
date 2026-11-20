# Example 6 (Intermediate-Hard) MINI PROJECT 1: Multiplication table generator
print("=== MULTIPLICATION TABLE GENERATOR ===")
number = int(input("Which table do you want? "))
start = int(input("Start at: "))
end = int(input("End at: "))

print(f"\n--- {number} times table ({start} to {end}) ---")
for i in range(start, end + 1):
    print(f"{number} x {i:>2} = {number * i:>4}")

# Bonus: a full grid (a loop inside a loop; you will master this in Topic 08)
print("\nQuick grid (1 to 5):")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:>4}", end="")
    print()                       # new line after each row
