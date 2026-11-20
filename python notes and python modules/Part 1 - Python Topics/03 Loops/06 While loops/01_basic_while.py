# Example 1 (Easy): The three parts of a while loop
#   1. a STARTING value        2. a CONDITION        3. a CHANGE inside the loop
count = 1                       # 1. start

while count <= 5:               # 2. keep going while this is True
    print("Count is", count)
    count += 1                  # 3. change (without this the loop never ends!)

print("Loop finished. count is now", count)

# WARNING: an infinite loop happens when the condition never becomes False.
# Press Ctrl + C in the terminal to stop one.
