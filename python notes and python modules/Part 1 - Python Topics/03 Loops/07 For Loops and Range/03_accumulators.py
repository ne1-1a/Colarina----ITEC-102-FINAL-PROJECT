# Example 3 (Intermediate): Totals, products and counters with for + range
n = 10

# Sum of 1 to n
total = 0
for i in range(1, n + 1):          # n + 1 because stop is excluded
    total += i
print(f"Sum of 1 to {n} = {total}")

# Factorial: 6! = 1 x 2 x 3 x 4 x 5 x 6
factorial = 1
for i in range(1, 7):
    factorial *= i
print("6! =", factorial)

# Sum of only the even numbers up to 20
even_total = 0
for i in range(2, 21, 2):
    even_total += i
print("Sum of evens up to 20 =", even_total)

# Count how many multiples of 3 are below 50
multiples = 0
for i in range(1, 50):
    if i % 3 == 0:
        multiples += 1
print("Multiples of 3 below 50:", multiples)

# Average of the first 5 odd numbers (1, 3, 5, 7, 9)
odd_total = 0
for i in range(1, 10, 2):
    odd_total += i
print("Average of first 5 odd numbers =", odd_total / 5)
