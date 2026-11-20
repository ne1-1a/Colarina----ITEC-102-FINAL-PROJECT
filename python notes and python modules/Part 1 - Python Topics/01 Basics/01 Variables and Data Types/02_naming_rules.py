# Example 2 (Easy): Naming rules and multiple assignment

# GOOD names: start with a letter or _, then letters, digits or _
first_name = "Alex"
student_2 = "Sam"
_secret = 42
total_score = 95        # snake_case is the Python style

# BAD names (they cause errors, so they are commented out):
# 2nd_student = "Sam"   # cannot start with a number
# my-name = "Alex"      # no dashes
# total score = 95      # no spaces
# class = "A"           # cannot use Python keywords (class, if, for, while...)

# Python is case-sensitive: these are 3 DIFFERENT variables
score = 1
Score = 2
SCORE = 3
print(score, Score, SCORE)

# Give the same value to many variables at once
x = y = z = 0
print(x, y, z)

# Swap two variables
left = "L"
right = "R"
left, right = right, left
print(left, right)
