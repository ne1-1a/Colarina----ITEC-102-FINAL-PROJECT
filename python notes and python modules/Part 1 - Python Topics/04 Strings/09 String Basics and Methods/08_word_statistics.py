# Example 8 (Hard) MINI PROJECT 3: Word statistics - count everything without split()
text = input("Type a sentence: ")

letters = 0
vowels = 0
digits = 0
spaces = 0
symbols = 0

for character in text:
    if character.isalpha():
        letters += 1
        if character.lower() in "aeiou":
            vowels += 1
    elif character.isdigit():
        digits += 1
    elif character == " ":
        spaces += 1
    else:
        symbols += 1

# Count words by walking through the text and building each word.
# We add one extra space at the end so the LAST word also gets counted.
word_count = 0
current_word = ""
longest_word = ""

for character in text + " ":
    if character.isalnum() or character == "'":
        current_word += character
    else:
        if current_word != "":
            word_count += 1
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""

# Palindrome check: ignore spaces, symbols and capital letters
only_letters = ""
for character in text.lower():
    if character.isalnum():
        only_letters += character
is_palindrome = only_letters != "" and only_letters == only_letters[::-1]

print()
print("=== STATISTICS ===")
print(f"Characters   : {len(text)}")
print(f"Words        : {word_count}")
print(f"Longest word : {longest_word}")
print(f"Letters      : {letters} (vowels {vowels}, consonants {letters - vowels})")
print(f"Digits       : {digits}")
print(f"Spaces       : {spaces}")
print(f"Symbols      : {symbols}")
print(f"Reversed     : {text[::-1]}")
print(f"Palindrome?  : {is_palindrome}")
