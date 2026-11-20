# Example 2 (Easy-Intermediate): continue - skip the REST of this round only

# Skip multiples of 3 (the loop keeps going)
print("1 to 10 without multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue                   # jump straight to the next i
    print(i, end=" ")
print()

# Ignore bad data but keep going
print("\nAdding only the positive numbers:")
total = 0
for value in range(-3, 4):         # -3, -2, -1, 0, 1, 2, 3
    if value <= 0:
        continue
    total += value
print("Sum of positives:", total)

# CAREFUL with while: update the counter BEFORE continue, or you loop forever
n = 0
while n < 10:
    n += 1                         # update first!
    if n % 2 == 0:
        continue
    print(n, end=" ")
print("<- odd numbers up to 10")
