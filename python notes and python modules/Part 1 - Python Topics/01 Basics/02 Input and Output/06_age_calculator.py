# Example 6 (Intermediate): Age calculator
CURRENT_YEAR = 2026

name = input("Your name: ")
birth_year = int(input("Year you were born: "))

age = CURRENT_YEAR - birth_year
year_turn_100 = birth_year + 100
years_left = year_turn_100 - CURRENT_YEAR

print()
print(f"Hi {name}! This year you turn {age}.")
print(f"You will turn 100 in {year_turn_100}, which is {years_left} years from now.")
