# Example 5 (Intermediate): Nested if - a decision INSIDE a decision
CORRECT_USER = "admin"
CORRECT_PASSWORD = "python123"

username = input("Username: ")

if username == CORRECT_USER:
    password = input("Password: ")
    if password == CORRECT_PASSWORD:
        print("Login successful. Welcome!")
        role = input("Are you a teacher? (yes/no): ").lower()
        if role == "yes":
            print("Opening the teacher dashboard...")
        else:
            print("Opening the student dashboard...")
    else:
        print("Wrong password.")
else:
    print("Unknown username.")
