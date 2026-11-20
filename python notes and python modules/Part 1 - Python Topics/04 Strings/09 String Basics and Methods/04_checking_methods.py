# Example 4 (Intermediate): Methods that answer True / False about a string
print("'12345'.isdigit()      :", "12345".isdigit())
print("'123a'.isdigit()       :", "123a".isdigit())
print("'abc'.isalpha()        :", "abc".isalpha())
print("'abc123'.isalpha()     :", "abc123".isalpha())
print("'abc123'.isalnum()     :", "abc123".isalnum())
print("'ABC'.isupper()        :", "ABC".isupper())
print("'abc'.islower()        :", "abc".islower())
print("'   '.isspace()        :", "   ".isspace())
print("'Hello World'.istitle():", "Hello World".istitle())

# Real use: figure out what the user typed
entry = input("\nType anything: ").strip()

if entry == "":
    print("You typed nothing.")
elif entry.isdigit():
    print("That is a whole number:", int(entry))
elif entry.isalpha():
    print("That is only letters:", entry.title())
elif entry.isalnum():
    print("Letters AND numbers mixed:", entry)
else:
    print("It has spaces or symbols in it.")
