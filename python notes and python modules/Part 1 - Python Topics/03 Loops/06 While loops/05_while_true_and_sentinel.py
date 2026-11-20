# Example 5 (Intermediate): while True + break, and sentinel loops

# Part 1: password with limited attempts
CORRECT_PASSWORD = "python123"
MAX_ATTEMPTS = 3
attempts = 0

while True:                                   # loop "forever" ... until break
    attempt = input("Password: ")
    attempts += 1

    if attempt == CORRECT_PASSWORD:
        print("Access granted!")
        break                                 # leave the loop immediately

    remaining = MAX_ATTEMPTS - attempts
    if remaining == 0:
        print("Too many wrong tries. Account locked.")
        break
    print(f"Wrong password. {remaining} attempt(s) left.")

# Part 2: sentinel loop - a special value (0) means "I am done"
print("\nAdd numbers. Type 0 to finish.")
total = 0
number = int(input("Number: "))
while number != 0:
    total += number
    number = int(input("Number: "))
print("Total:", total)
