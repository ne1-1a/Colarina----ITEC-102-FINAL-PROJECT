# Example 1 (Easy): A simple if - run code ONLY when the condition is True
age = 20

if age >= 18:
    print("You are an adult.")          # indented = belongs to the if

print("This line always runs.")         # not indented = always runs

temperature = 35
if temperature > 30:
    print("It is hot today!")
    print("Drink plenty of water.")

# When the condition is False, the whole block is skipped
if temperature < 10:
    print("This will NOT print.")
