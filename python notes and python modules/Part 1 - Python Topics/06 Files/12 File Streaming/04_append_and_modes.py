# Example 4 (Intermediate): The file modes "w" vs "a" vs "r"


def show(filename):
    print(f"--- {filename} ---")
    with open(filename) as file:
        for line in file:
            print("  ", line.strip())


# "w" starts a fresh file
with open("demo_shopping.txt", "w") as file:
    file.write("Rice\n")
    file.write("Eggs\n")
print("After first 'w':")
show("demo_shopping.txt")

# "a" = append: ADD to the end and keep the old content
with open("demo_shopping.txt", "a") as file:
    file.write("Milk\n")
    file.write("Bread\n")
print("\nAfter 'a':")
show("demo_shopping.txt")

# Running the same append twice adds the lines twice
with open("demo_shopping.txt", "a") as file:
    print("Coffee", file=file)
print("\nAfter another 'a':")
show("demo_shopping.txt")

# DANGER: opening with "w" again ERASES everything that was there
with open("demo_shopping.txt", "w") as file:
    file.write("Only this is left\n")
print("\nAfter 'w' again (old content is gone!):")
show("demo_shopping.txt")

# Summary
#   "r" read (file must exist)   "w" write (erases)   "a" append (keeps old content)
