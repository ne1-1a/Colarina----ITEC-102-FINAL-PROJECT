# Example 1 (Easy): match / case with numbers
# NOTE: match needs Python 3.10 or newer.
day_number = int(input("Enter a day number (1-7): "))

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:                       # _ = "anything else" (the default)
        print("Invalid day number")
