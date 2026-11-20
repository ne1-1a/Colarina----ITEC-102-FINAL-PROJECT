# Example 3 (Easy-Intermediate): Comparison operators always give True or False
x = 10
y = 20

print("x == y :", x == y)     # equal to
print("x != y :", x != y)     # not equal to
print("x < y  :", x < y)
print("x > y  :", x > y)
print("x <= 10:", x <= 10)
print("y >= 25:", y >= 25)

# = stores a value, == asks a question. Do not mix them up!
answer = (x == 10)
print("Is x equal to 10?", answer)

# Comparing text
print("apple" == "apple")
print("apple" == "Apple")      # capital letters matter
print("apple" < "banana")      # alphabetical order
print("Zebra" < "apple")       # capitals come BEFORE lower-case letters
