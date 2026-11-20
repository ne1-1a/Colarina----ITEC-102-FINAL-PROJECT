# Example 8 (Hard): Student profile card - many types, many calculations
CURRENT_YEAR = 2026

full_name = "Alex Rivera"
birth_year = 2007
height_m = 1.68
weight_kg = 58.5
course = "BS Computer Science"
units = 21
has_scholarship = False

# Calculated values
age = CURRENT_YEAR - birth_year
is_adult = age >= 18
bmi = weight_kg / height_m ** 2
graduation_year = CURRENT_YEAR + 4
years_to_25 = 25 - age
full_load = units >= 18

print("+" + "-" * 38 + "+")
print(f"| {'STUDENT PROFILE CARD':^36} |")
print("+" + "-" * 38 + "+")
print(f"| Name        : {full_name:<22} |")
print(f"| Course      : {course:<22} |")
print(f"| Age         : {age:<22} |")
print(f"| Adult?      : {str(is_adult):<22} |")
print(f"| BMI         : {bmi:<22.1f} |")
print(f"| Units       : {units:<22} |")
print(f"| Full load?  : {str(full_load):<22} |")
print(f"| Scholarship : {str(has_scholarship):<22} |")
print(f"| Graduates   : {graduation_year:<22} |")
print(f"| Turns 25 in : {years_to_25} years{'':<14} |")
print("+" + "-" * 38 + "+")
