# Example 8 (Hard): Final grade computer - input, casting and every operator type
print("=== FINAL GRADE COMPUTER ===")
quiz = float(input("Quiz average    (0-100): "))
project = float(input("Project score   (0-100): "))
exam = float(input("Exam score      (0-100): "))

# Weighted average: quiz 30%, project 30%, exam 40%
final = quiz * 0.30 + project * 0.30 + exam * 0.40

passed = final >= 75
with_honors = final >= 90 and exam >= 85
perfect_exam = exam == 100
needs_retake = not passed or exam < 50

print()
print(f"Final grade   : {final:.2f}")
print(f"Rounded       : {round(final)}")
print(f"Whole number  : {int(final)}")
print(f"Passed?       : {passed}")
print(f"With honors?  : {with_honors}")
print(f"Perfect exam? : {perfect_exam}")
print(f"Needs retake? : {needs_retake}")
print(f"Points to 100 : {100 - final:.2f}")
