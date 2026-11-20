# Example 8 (Hard): Registration form with a formatted summary card
CURRENT_YEAR = 2026

print("=== STUDENT REGISTRATION ===")
full_name = input("Full name           : ")
birth_year = int(input("Birth year          : "))
course = input("Course              : ")
gpa = float(input("GPA (1.0 - 5.0)     : "))
years_left = int(input("Years until graduating: "))

age = CURRENT_YEAR - birth_year
graduation_year = CURRENT_YEAR + years_left

print()
print("+" + "=" * 38 + "+")
print("|" + "REGISTRATION SUMMARY".center(38) + "|")
print("+" + "=" * 38 + "+")
print(f"| {'Name':<12}: {full_name:<23} |")
print(f"| {'Age':<12}: {age:<23} |")
print(f"| {'Course':<12}: {course:<23} |")
print(f"| {'GPA':<12}: {gpa:<23.2f} |")
print(f"| {'Graduation':<12}: {graduation_year:<23} |")
print("+" + "=" * 38 + "+")
print(f"Welcome, {full_name.split()[0]}!")
