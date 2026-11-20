# Example 5 (Intermediate): Looping through a string, one character at a time
word = "Programming"

# 1. Direct loop
for letter in word:
    print(letter, end=" ")
print()

# 2. Count vowels
vowels = 0
for letter in word.lower():
    if letter in "aeiou":
        vowels += 1
print("Vowels:", vowels, "| Consonants:", len(word) - vowels)

# 3. Reverse a string by hand
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word      # put each new letter in FRONT
print("Reversed:", reversed_word)

# 4. Loop with the index when you need the position
for i in range(len(word)):
    if i % 2 == 0:
        print(f"index {i}: {word[i]}")

# 5. ord() gives a letter's number, chr() turns a number back into a letter
print(ord("a"), ord("A"), chr(100))

# 6. Caesar cipher: shift each letter forward by 3
secret = ""
for letter in "hello":
    shifted = (ord(letter) - ord("a") + 3) % 26     # wraps z -> c
    secret += chr(shifted + ord("a"))
print("hello ->", secret)
