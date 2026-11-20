# Example 5 (Intermediate-Hard): lambda, functions as values, and built-in helpers

# lambda = a tiny one-line function with no name
square = lambda x: x * x
add = lambda a, b: a + b
is_adult = lambda age: age >= 18

print(square(6), add(2, 3), is_adult(17))

# Same as:   def square(x): return x * x


# Functions are values: you can pass them into other functions
def apply_twice(func, value):
    return func(func(value))


print("square twice on 3 =", apply_twice(square, 3))        # (3*3)*(3*3) = 81


def apply_operation(func, a, b):
    return func(a, b)


print(apply_operation(add, 2, 3))
print(apply_operation(lambda a, b: a * b, 4, 5))             # lambda written on the spot
print(apply_operation(lambda a, b: a ** b, 2, 10))


# A function that RETURNS a function
def make_multiplier(factor):
    return lambda x: x * factor


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))

# Python already has many useful built-in functions
print("max(3, 9, 4)       :", max(3, 9, 4))
print("min(3, 9, 4)       :", min(3, 9, 4))
print("abs(-7.5)          :", abs(-7.5))
print("round(3.14159, 2)  :", round(3.14159, 2))
print("pow(2, 10)         :", pow(2, 10))
print("divmod(17, 5)      :", divmod(17, 5))
print("len('Python')      :", len("Python"))
print("sum(range(1, 11))  :", sum(range(1, 11)))
