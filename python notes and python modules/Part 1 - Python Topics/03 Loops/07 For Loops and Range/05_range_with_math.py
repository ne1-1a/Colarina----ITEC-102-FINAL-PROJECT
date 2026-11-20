# Example 5 (Intermediate): Math patterns with range()

print("Squares of 1 to 10:")
for i in range(1, 11):
    print(i * i, end=" ")

print("\n\nPowers of 2:")
for power in range(0, 11):
    print(2 ** power, end=" ")

print("\n\nMultiples of 7 up to 70:")
for i in range(7, 71, 7):
    print(i, end=" ")

print("\n\nCelsius to Fahrenheit:")
for celsius in range(0, 101, 20):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:>3} C = {fahrenheit:>5.1f} F")

print("\nFizzBuzz (1 to 15):")
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
