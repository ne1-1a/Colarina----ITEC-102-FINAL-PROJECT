# Example 3 (Easy-Intermediate): if / elif / else - choose between MANY paths
# Python checks from the top and stops at the FIRST True condition.
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} -> Grade {grade}")

# Why order matters: with 95, "score >= 60" would also be True,
# but Python never reaches it because "score >= 90" matched first.
