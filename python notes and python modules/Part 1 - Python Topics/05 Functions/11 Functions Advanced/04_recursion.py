# Example 4 (Intermediate-Hard): Recursion - a function that calls ITSELF
# Every recursive function needs:  1) a BASE CASE (when to stop)
#                                   2) a step that moves toward the base case


def countdown(n):
    if n == 0:                       # base case
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)                 # smaller problem


countdown(3)


def factorial(n):
    if n <= 1:                       # base case
        return 1
    return n * factorial(n - 1)


print("5! =", factorial(5))


def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)


print("Sum 1 to 10 =", sum_to(10))


def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


print("Digit sum of 4829 =", digit_sum(4829))


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print("2 to the 8th =", power(2, 8))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("First 10 Fibonacci numbers:", end=" ")
for i in range(10):
    print(fibonacci(i), end=" ")
print()


def gcd(a, b):                       # Euclid's algorithm
    if b == 0:
        return a
    return gcd(b, a % b)


print("GCD of 48 and 18 =", gcd(48, 18))


# Watch the calls pile up and unwind
def factorial_trace(n, depth=0):
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    if n <= 1:
        print(f"{indent}-> returns 1")
        return 1
    result = n * factorial_trace(n - 1, depth + 1)
    print(f"{indent}-> returns {result}")
    return result


factorial_trace(4)

# Python stops runaway recursion at about 1000 calls (RecursionError)
