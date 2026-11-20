# Example 6 (Intermediate-Hard) MINI PROJECT 1: Menu calculator
while True:
    print("\n=== CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose (1-5): ").strip()

    # First match: exit, valid operation, or invalid choice
    match choice:
        case "5":
            print("Goodbye!")
            break
        case "1" | "2" | "3" | "4":
            pass                      # valid, keep going and ask for the numbers
        case _:
            print("Please choose 1 to 5.")
            continue                  # go back to the top of the loop

    a = float(input("First number : "))
    b = float(input("Second number: "))

    # Second match: do the chosen operation
    match choice:
        case "1":
            print(f"{a} + {b} = {a + b}")
        case "2":
            print(f"{a} - {b} = {a - b}")
        case "3":
            print(f"{a} x {b} = {a * b}")
        case "4":
            if b == 0:
                print("Cannot divide by zero!")
            else:
                print(f"{a} / {b} = {a / b:.2f}")
