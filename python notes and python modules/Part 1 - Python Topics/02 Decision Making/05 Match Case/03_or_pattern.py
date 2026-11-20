# Example 3 (Easy-Intermediate): The | (OR) pattern - several values, one case
letter = input("Type a letter: ").strip().lower()

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print(letter, "is a vowel")
    case _:
        print(letter, "is not a vowel")

day = int(input("Day number (1-7): "))

match day:
    case 6 | 7:
        print("Weekend: sleep in!")
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday: time for class.")
    case _:
        print("Invalid day")
