# Example 3 (Intermediate): The most useful string methods
text = "  Hello, Python World!  "

# Cleaning
print(repr(text))                # repr() shows the hidden spaces
print(repr(text.strip()))        # removes spaces at BOTH ends
print(repr(text.lstrip()))       # left only
print(repr(text.rstrip()))       # right only

clean = text.strip()

# Changing case
print(clean.upper())
print(clean.lower())
print(clean.title())             # Each Word Capitalized
print(clean.capitalize())        # First letter only
print(clean.swapcase())

# Searching
print(clean.count("o"))                 # how many times?
print(clean.find("Python"))             # index where it starts
print(clean.find("Java"))               # -1 means "not found"
print(clean.startswith("Hello"))
print(clean.endswith("!"))

# Replacing
print(clean.replace("Python", "Java"))
print("2026-11-19".replace("-", "/"))

# IMPORTANT: methods return a NEW string. The original never changes.
original = "python"
original.upper()                 # result thrown away!
print(original)                  # still python
original = original.upper()      # store the result to keep it
print(original)

# Chaining methods: left to right
print("  mIxEd   CaSe  ".strip().lower().title())
