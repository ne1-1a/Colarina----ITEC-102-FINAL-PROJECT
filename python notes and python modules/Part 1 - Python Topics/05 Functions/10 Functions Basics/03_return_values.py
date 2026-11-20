# Example 3 (Intermediate): return - give a value BACK to the caller
# print() only SHOWS something. return HANDS BACK a value you can keep using.


def square(n):
    return n * n


result = square(5)
print("square(5) =", result)
print("square(3) + square(4) =", square(3) + square(4))     # use results in math


def show_square(n):
    print(n * n)                    # prints, but returns nothing


x = show_square(4)
print("What did show_square give back?", x)                 # None


def is_even(n):
    return n % 2 == 0               # returns True or False


print(is_even(10), is_even(7))


def get_grade(score):
    # return ends the function immediately, so we need no elif/else
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"


print(get_grade(95), get_grade(82), get_grade(40))


def absolute(n):
    if n < 0:
        return -n
    return n


print(absolute(-8), absolute(8))
