# Example 2 (Easy): Escape characters and decorating output
print("Line 1\nLine 2")            # \n = new line
print("Name:\tAlex")               # \t = tab
print("She said \"hi\"")           # \" = a quote inside a quote
print('It\'s fine')                # \' = an apostrophe inside single quotes
print("It's easier with double quotes")
print("C:\\Users\\Alex")           # \\ = one backslash
print(r"C:\Users\new")             # r"..." = raw string, backslashes stay as they are

# Decorating output with string tricks
print("=" * 30)
print("MENU".center(30))
print("=" * 30)
print("1. Start".ljust(15) + "2. Quit")
print("-" * 30)

print("""This is a
multi-line
message.""")
