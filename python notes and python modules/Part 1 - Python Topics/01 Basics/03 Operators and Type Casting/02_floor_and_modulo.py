# Example 2 (Easy-Intermediate): // and % are more useful than they look

# 1. Even or odd? Even numbers have remainder 0 when divided by 2
number = 27
print(number, "is even?", number % 2 == 0)

# 2. Minutes -> hours and minutes
total_minutes = 275
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes = {hours} h {minutes} min")

# 3. Pull digits out of a number
n = 4829
print("Last digit        :", n % 10)
print("Without last digit:", n // 10)

# 4. Wrap around (days of the week repeat every 7)
day_number = 10
print("Day 10 is day", day_number % 7, "of the week cycle")

# 5. How many bills do we need? (chain // and %)
amount = 1287
thousands = amount // 1000
rest = amount % 1000
fives = rest // 500
rest = rest % 500
hundreds = rest // 100
rest = rest % 100
print(f"PHP {amount} = {thousands} x 1000, {fives} x 500, {hundreds} x 100, and PHP {rest} left")
