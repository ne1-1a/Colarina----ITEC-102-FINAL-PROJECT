# Example 6 (Intermediate-Hard) MINI PROJECT 1: Number guessing game
# (The secret is fixed here. In the modules topic you can use random.randint(1, 100).)
SECRET = 37
MAX_ATTEMPTS = 7

print("=== GUESS THE NUMBER (1-100) ===")
print(f"You have {MAX_ATTEMPTS} attempts.")

attempts = 0
won = False

while attempts < MAX_ATTEMPTS and not won:
    guess = int(input(f"\nAttempt {attempts + 1}: "))
    attempts += 1

    if guess == SECRET:
        won = True
    elif abs(guess - SECRET) <= 5:
        print("Very close!", "Go higher." if guess < SECRET else "Go lower.")
    elif guess < SECRET:
        print("Too low. Go higher.")
    else:
        print("Too high. Go lower.")

print()
if won:
    print(f"You got it in {attempts} attempt(s)!")
else:
    print(f"Out of attempts. The number was {SECRET}.")
