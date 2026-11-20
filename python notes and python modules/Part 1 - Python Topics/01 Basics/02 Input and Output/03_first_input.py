# Example 3 (Easy): input() - talk to the user
name = input("What is your name? ")
print("Hello,", name + "!")

subject = input("What is your favorite subject? ")
print(f"{name} likes {subject}.")

# Whatever the user types is TEXT (str), even if they type digits
print("Type of what you typed:", type(name).__name__)
