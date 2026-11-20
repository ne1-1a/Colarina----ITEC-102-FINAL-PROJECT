# Example 6 (Intermediate-Hard) MINI PROJECT 1: Name formatter
raw = input("Enter a full name (any messy style): ")

# Step 1: collapse extra spaces and fix the capital letters.
# split() breaks text into words, " ".join(...) glues them back with ONE space.
cleaned = " ".join(raw.split()).title()

if cleaned == "":
    print("You did not type a name.")
else:
    # Step 2: separate the last name from the first names using the LAST space
# (Limitation: this treats the last WORD as the last name, so a compound surname
#  like "Dela Cruz" gets split. Fixing that needs extra rules, a good challenge!)
    last_space = cleaned.rfind(" ")
    if last_space == -1:                       # only one word
        first_names = cleaned
        last_name = ""
    else:
        first_names = cleaned[:last_space]
        last_name = cleaned[last_space + 1:]

    # Step 3: initials = first letter of every word
    initials = ""
    previous = " "
    for character in cleaned:
        if previous == " " and character != " ":
            initials += character + "."
        previous = character

    letters_only = cleaned.replace(" ", "")

    print()
    print("Cleaned      :", cleaned)
    if last_name != "":
        print("Last, First  :", f"{last_name}, {first_names}")
    print("Initials     :", initials)
    print("UPPERCASE    :", cleaned.upper())
    print("Letter count :", len(letters_only))
