# Example 1 (Easy): Create a text file and write into it
# After running, open demo_story.txt, demo_numbers.txt and demo_names.txt to see the results.

# open(filename, mode): "w" = write mode.
# It CREATES the file, or ERASES it if it already exists!
file = open("demo_story.txt", "w")
file.write("Once upon a time,\n")
file.write("there was a Python programmer.\n")
file.write("The end.")
file.close()                          # always close the file when you are done
print("Created demo_story.txt")

# write() does NOT add a new line for you. Add "\n" yourself.
# write() also accepts TEXT only, so numbers must be converted with str().
file = open("demo_numbers.txt", "w")
for number in range(1, 6):
    file.write(str(number) + "\n")
file.close()
print("Created demo_numbers.txt with the numbers 1 to 5")

# print(..., file=file) writes like print() does, and adds the new line for you
file = open("demo_names.txt", "w")
print("Alex", file=file)
print("Sam", file=file)
print("Jordan", file=file)
file.close()
print("Created demo_names.txt")
