# Example 7 (Hard) MINI PROJECT 2: Grade calculator
print("=== GRADE CALCULATOR ===")
subjects = int(input("How many subjects? "))

if subjects <= 0:
    print("You need at least one subject.")
else:
    total = 0
    highest = 0
    lowest = 100
    passed = 0

    for i in range(1, subjects + 1):
        grade = float(input(f"Grade for subject {i}: "))
        total += grade
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade
        if grade >= 75:
            passed += 1

    average = total / subjects

    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 75:
        letter = "C"
    else:
        letter = "F"

    print()
    print("=== RESULT ===")
    print(f"Average       : {average:.2f} ({letter})")
    print(f"Highest       : {highest}")
    print(f"Lowest        : {lowest}")
    print(f"Subjects passed: {passed} of {subjects}")
