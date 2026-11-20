# Example 1 (Easy): Creating and combining strings
first = "Python"
second = 'is fun'

sentence = first + " " + second          # + glues strings together (concatenation)
print(sentence)
print("Length of the sentence:", len(sentence))   # len() counts EVERY character, spaces too

print("Ha" * 3)                          # * repeats a string
print("-" * 20)

name = "Alex"
age = 19
print("Hello, " + name + "!")
print("Age: " + str(age))                # + only works with strings, so convert numbers with str()
print(f"{name} is {age} years old")      # f-strings do the converting for you

# in / not in : is this text inside that text?
print("Py" in sentence)
print("Java" in sentence)
print("Java" not in sentence)

# An empty string has length 0 and counts as False
empty = ""
print(len(empty), bool(empty))

# Special characters count as ONE character each
print(len("Hello\n"))
