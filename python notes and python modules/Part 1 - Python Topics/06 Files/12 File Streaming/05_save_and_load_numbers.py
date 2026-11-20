# Example 5 (Intermediate): Saving numbers and checking a file exists first
import os            # os is explained in Part 2; here we only use it to check files

# Save scores, one per line
with open("demo_scores.txt", "w") as file:
    for score in range(70, 100, 7):          # 70, 77, 84, 91, 98
        file.write(str(score) + "\n")

# Load them back: everything in a file is TEXT, so convert with int() / float()
total = 0
count = 0
with open("demo_scores.txt") as file:
    for line in file:
        total += int(line)                   # int() ignores the "\n" at the end
        count += 1
print(f"Loaded {count} scores. Total = {total}, average = {total / count:.1f}")

# Opening a file that does not exist crashes the program (FileNotFoundError).
# Check first with os.path.exists().
filename = "demo_highscore.txt"
if os.path.exists(filename):
    with open(filename) as file:
        high_score = int(file.read())
    print("Loaded the saved high score:", high_score)
else:
    high_score = 0
    print("No saved high score yet, starting at 0")

# A tiny high-score saver
new_score = 120
if new_score > high_score:
    with open(filename, "w") as file:
        file.write(str(new_score))
    print(f"NEW HIGH SCORE: {new_score}! Saved to {filename}")
else:
    print(f"{new_score} did not beat the high score of {high_score}")

print("Run this file again to see the saved high score being loaded.")
