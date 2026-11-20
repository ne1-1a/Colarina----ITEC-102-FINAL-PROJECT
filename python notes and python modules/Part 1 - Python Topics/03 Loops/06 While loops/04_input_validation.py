# Example 4 (Intermediate): Keep asking until the answer is valid
age_text = input("Enter your age (1-120): ")

# isdigit() is True only if the text is made of digits (so "abc" and "-5" fail).
# Because of "or", int() only runs when isdigit() is True, so it never crashes.
while not age_text.isdigit() or int(age_text) < 1 or int(age_text) > 120:
    print("Invalid! Please enter a whole number from 1 to 120.")
    age_text = input("Enter your age (1-120): ")

age = int(age_text)
print("Thank you! Age saved:", age)

# Same idea with text answers
answer = input("Do you want to continue? (yes/no): ").strip().lower()
while answer != "yes" and answer != "no":
    print("Please type yes or no.")
    answer = input("Do you want to continue? (yes/no): ").strip().lower()
print("You answered:", answer)
