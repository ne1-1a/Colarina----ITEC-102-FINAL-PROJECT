# Example 8 (Hard) MINI PROJECT 3: Number analyzer (sentinel loop + many trackers)
print("=== NUMBER ANALYZER ===")
print("Enter whole numbers. Type 0 to finish.\n")

count = 0
total = 0
largest = None       # None = "no number yet"
smallest = None
even_count = 0
odd_count = 0

number = int(input("Number: "))
while number != 0:
    count += 1
    total += number

    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    number = int(input("Number: "))

print()
if count == 0:
    print("You did not enter any numbers.")
else:
    print("=== REPORT ===")
    print(f"How many   : {count}")
    print(f"Sum        : {total}")
    print(f"Average    : {total / count:.2f}")
    print(f"Largest    : {largest}")
    print(f"Smallest   : {smallest}")
    print(f"Even / Odd : {even_count} / {odd_count}")
