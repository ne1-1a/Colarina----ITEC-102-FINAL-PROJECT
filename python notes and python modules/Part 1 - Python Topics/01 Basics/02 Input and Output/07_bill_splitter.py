# Example 7 (Intermediate): Restaurant bill splitter
print("=== BILL SPLITTER ===")
bill = float(input("Total bill (PHP): "))
tip_percent = float(input("Tip percent (e.g. 10): "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
each = total / people

print()
print(f"Bill        : PHP {bill:>10,.2f}")
print(f"Tip ({tip_percent:.0f}%)    : PHP {tip:>10,.2f}")
print(f"Grand total : PHP {total:>10,.2f}")
print("-" * 30)
print(f"Each of {people} pays: PHP {each:,.2f}")
