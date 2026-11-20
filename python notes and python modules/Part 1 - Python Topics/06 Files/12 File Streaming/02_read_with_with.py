# Example 2 (Easy-Intermediate): Read a file, and the safe "with" way of opening
# Setup: make a small file to read
with open("demo_story.txt", "w") as file:
    file.write("Once upon a time,\nthere was a Python programmer.\nThe end.")

# "with" closes the file AUTOMATICALLY when the indented block ends,
# even if something goes wrong inside. Use it every time.
with open("demo_story.txt", "r") as file:       # "r" = read mode (this is the default)
    content = file.read()                       # read() returns EVERYTHING as one string

print(content)
print("\nIs the file closed now?", file.closed)

# read(n) reads only n characters, and the next read continues where the last stopped
with open("demo_story.txt") as file:
    print("First 4 characters :", repr(file.read(4)))
    print("Next 5 characters  :", repr(file.read(5)))

# readline() reads ONE line (including its "\n")
with open("demo_story.txt") as file:
    first = file.readline()
    second = file.readline()
    print("Line 1:", repr(first))
    print("Line 2:", repr(second))
    print("Line 3:", repr(file.readline()))
    print("After the end:", repr(file.readline()))     # empty string means "nothing left"
