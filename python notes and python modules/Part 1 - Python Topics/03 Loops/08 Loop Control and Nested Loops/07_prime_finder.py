# Example 7 (Hard): Prime number finder (nested loops + break + for/else)
# A prime has no divisors except 1 and itself.
LIMIT = 50
count = 0

print(f"Prime numbers up to {LIMIT}:")
for number in range(2, LIMIT + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break                  # found a divisor, so it is NOT prime
    else:
        # the for loop ended without break -> no divisor found -> prime
        print(number, end=" ")
        count += 1

print(f"\n\nThere are {count} primes up to {LIMIT}.")

# Largest prime below 100
largest = 0
for number in range(2, 100):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        largest = number
print("Largest prime below 100:", largest)
