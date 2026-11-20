# Example 1 (Easy): break - leave the loop immediately

# Find the first multiple of 7 above 50, then stop searching
for number in range(51, 100):
    if number % 7 == 0:
        print("First multiple of 7 above 50:", number)
        break                      # no need to check 57, 58, 59...

# break in a while loop: stop when the user types a keyword
total = 0
while True:
    text = input("Enter a number (or type 'stop'): ")
    if text == "stop":
        break
    total += int(text)
print("Total so far:", total)
