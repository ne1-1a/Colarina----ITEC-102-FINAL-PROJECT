# Example 3 (Intermediate): STREAMING - loop through a file one line at a time
# Setup
with open("demo_poem.txt", "w") as file:
    file.write("Roses are red,\n")
    file.write("Violets are blue,\n")
    file.write("Python is fun,\n")
    file.write("And so are you.\n")

# "for line in file" streams the file: Python holds only ONE line in memory at a time,
# so it works even for files that are gigabytes big.
print("--- Raw lines (each line already ends with \\n) ---")
with open("demo_poem.txt") as file:
    for line in file:
        print(line)                      # extra blank lines appear

print("--- Cleaned with strip() ---")
with open("demo_poem.txt") as file:
    for line in file:
        print(line.strip())

print("--- Numbered ---")
with open("demo_poem.txt") as file:
    number = 0
    for line in file:
        number += 1
        print(f"{number:>2}: {line.strip()}")

print("--- Statistics ---")
lines = 0
characters = 0
longest = ""
with open("demo_poem.txt") as file:
    for line in file:
        text = line.strip()
        lines += 1
        characters += len(text)
        if len(text) > len(longest):
            longest = text
print("Lines          :", lines)
print("Characters     :", characters)
print("Longest line   :", longest)

print("--- Search: lines containing 'fun' or 'blue' ---")
with open("demo_poem.txt") as file:
    for line in file:
        if "fun" in line or "blue" in line:
            print("Found:", line.strip())
