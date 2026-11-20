# Example 7 (Hard) MINI PROJECT 2: Grade book saved as "name,grade" lines
import os

FILENAME = "gradebook.txt"


def is_number(text):
    """True for things like 85 or 88.5 (replace removes ONE dot before checking digits)."""
    return text.replace(".", "", 1).isdigit()


def add_student():
    name = input("Student name: ").strip()
    if name == "" or "," in name:
        print("Invalid name (it must not be empty or contain a comma).")
        return
    grade_text = input("Grade (0-100): ").strip()
    if not is_number(grade_text) or float(grade_text) > 100:
        print("Invalid grade.")
        return
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{name},{grade_text}\n")
    print(f"Saved {name}: {grade_text}")


def show_report():
    if not os.path.exists(FILENAME):
        print("No students yet.")
        return

    count = 0
    total = 0
    passed = 0
    highest = -1
    lowest = 101
    best_name = ""

    print(f"\n{'NAME':<20}{'GRADE':>8}")
    print("-" * 28)
    with open(FILENAME, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            comma = line.rfind(",")                 # split name and grade at the LAST comma
            name = line[:comma]
            grade = float(line[comma + 1:])

            print(f"{name:<20}{grade:>8.1f}")
            count += 1
            total += grade
            if grade >= 75:
                passed += 1
            if grade > highest:
                highest = grade
                best_name = name
            if grade < lowest:
                lowest = grade

    if count == 0:
        print("(no students)")
        return
    print("-" * 28)
    print(f"Students : {count}")
    print(f"Average  : {total / count:.2f}")
    print(f"Highest  : {highest:.1f} ({best_name})")
    print(f"Lowest   : {lowest:.1f}")
    print(f"Passed   : {passed} of {count} (75 and up)")


def clear_all():
    if input("Delete ALL students? (yes/no): ").strip().lower() == "yes":
        with open(FILENAME, "w", encoding="utf-8") as file:     # "w" erases the file
            pass
        print("Grade book cleared.")


def main():
    while True:
        print("\n=== GRADE BOOK ===")
        print("1. Add student")
        print("2. Show report")
        print("3. Clear all")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            clear_all()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1 to 4.")


main()
