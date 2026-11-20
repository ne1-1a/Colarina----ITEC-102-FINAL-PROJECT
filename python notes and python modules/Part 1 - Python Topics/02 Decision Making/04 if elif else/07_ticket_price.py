# Example 7 (Intermediate-Hard): Cinema ticket price - elif groups + extra discounts
BASE_PRICE = 300

age = int(input("Age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
is_tuesday = input("Is it Tuesday? (yes/no): ").lower() == "yes"

# Step 1: price by age group
if age <= 3:
    price = 0
    group = "Toddler (free)"
elif age <= 12:
    price = BASE_PRICE * 0.50
    group = "Child (50% off)"
elif age >= 60:
    price = BASE_PRICE * 0.80
    group = "Senior (20% off)"
else:
    price = BASE_PRICE
    group = "Regular"
    # Step 2: students only get a discount if they are in the regular group
    if is_student:
        price = price * 0.85
        group = "Student (15% off)"

# Step 3: Tuesday discount (but never go below zero)
tuesday_applied = False
if is_tuesday and price > 0:
    price = max(price - 50, 0)
    tuesday_applied = True

print()
print(f"Group                   : {group}")
print(f"Tuesday discount applied: {tuesday_applied}")
print(f"Pay                     : PHP {price:.2f}")
