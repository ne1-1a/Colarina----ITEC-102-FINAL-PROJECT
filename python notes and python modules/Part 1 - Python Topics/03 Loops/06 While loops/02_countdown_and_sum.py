# Example 2 (Easy-Intermediate): Counting down and adding up (accumulators)

# Countdown
countdown = 10
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("\nLiftoff!")

# Accumulator: a variable that collects a running total
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print("Sum of 1 to 100 =", total)

# Accumulator that multiplies: 5! = 5 x 4 x 3 x 2 x 1
product = 1
n = 5
while n > 1:
    product *= n
    n -= 1
print("5! =", product)

# While is great when you do NOT know how many repeats you need
savings = 1000.0
years = 0
while savings < 2000:
    savings *= 1.07            # grows 7% each year
    years += 1
print(f"At 7% a year, PHP 1,000 doubles after {years} years (PHP {savings:,.2f})")
