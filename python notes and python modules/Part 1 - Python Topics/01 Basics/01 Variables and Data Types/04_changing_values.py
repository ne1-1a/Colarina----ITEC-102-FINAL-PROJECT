# Example 4 (Easy-Intermediate): Variables can change

score = 10
print("Start        :", score)

score = 20
print("Replaced     :", score)

score = score + 5      # read the right side first, then store it back
print("Added 5      :", score)

score += 5             # shortcut for the line above
print("Using +=     :", score)

# A variable can even change type (allowed, but avoid it in real programs)
thing = 100
print(thing, type(thing).__name__)
thing = "now I am text"
print(thing, type(thing).__name__)

# CONSTANTS: UPPER_CASE names mean "please do not change me"
MAX_LIVES = 3
PI = 3.14159
lives = MAX_LIVES
lives -= 1
print("Lives left:", lives, "of", MAX_LIVES)

# del removes a variable completely
temporary = 5
del temporary
# print(temporary)   # would cause: NameError: name 'temporary' is not defined
