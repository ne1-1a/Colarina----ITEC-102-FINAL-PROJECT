# Example 3 (Intermediate): pass, and the strange but useful loop "else"

# pass = "do nothing here yet" (a placeholder so the code is valid)
for i in range(1, 6):
    if i == 3:
        pass                       # TODO: handle 3 later
    else:
        print(i, end=" ")
print()

# for ... else: the else block runs ONLY if the loop finished WITHOUT break
for number in range(100, 110):
    if number % 13 == 0:
        print("Found a multiple of 13:", number)
        break
else:
    print("No multiple of 13 between 100 and 109")

for number in range(100, 104):
    if number % 13 == 0:
        print("Found a multiple of 13:", number)
        break
else:
    print("No multiple of 13 between 100 and 103")

# while ... else works the same way
attempts = 0
while attempts < 3:
    attempts += 1
    if attempts == 5:              # never True, so break never happens
        break
else:
    print("while loop ended normally after", attempts, "attempts")
