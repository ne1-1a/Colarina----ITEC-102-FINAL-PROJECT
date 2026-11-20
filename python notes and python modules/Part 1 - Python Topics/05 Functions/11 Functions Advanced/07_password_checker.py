# Example 7 (Hard) MINI PROJECT 2: Password strength checker (functions + strings)


def long_enough(password, minimum=8):
    return len(password) >= minimum


def has_upper(password):
    for character in password:
        if character.isupper():
            return True
    return False


def has_lower(password):
    for character in password:
        if character.islower():
            return True
    return False


def has_digit(password):
    for character in password:
        if character.isdigit():
            return True
    return False


def has_symbol(password):
    for character in password:
        if not character.isalnum() and character != " ":
            return True
    return False


def strength_score(password):
    score = 0
    if long_enough(password):
        score += 1
    if has_upper(password):
        score += 1
    if has_lower(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_symbol(password):
        score += 1
    return score


def strength_label(score):
    if score == 5:
        return "VERY STRONG"
    if score == 4:
        return "STRONG"
    if score == 3:
        return "OKAY"
    return "WEAK"


def print_feedback(password):
    if not long_enough(password):
        print("  - use at least 8 characters")
    if not has_upper(password):
        print("  - add an UPPERCASE letter")
    if not has_lower(password):
        print("  - add a lowercase letter")
    if not has_digit(password):
        print("  - add a digit")
    if not has_symbol(password):
        print("  - add a symbol such as ! or @")


print("=== PASSWORD CHECKER ===")
print("Create a password that scores STRONG or better (type 'quit' to stop).")

while True:
    password = input("\nNew password: ")
    if password == "quit":
        print("Cancelled.")
        break

    score = strength_score(password)
    print(f"Score: {score}/5 -> {strength_label(score)}")

    if score >= 4:
        print("Password accepted!")
        break
    print("Try again. Tips:")
    print_feedback(password)
