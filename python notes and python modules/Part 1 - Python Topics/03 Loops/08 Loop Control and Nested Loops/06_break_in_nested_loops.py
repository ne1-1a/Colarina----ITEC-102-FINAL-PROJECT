# Example 6 (Intermediate-Hard): break only leaves the INNER loop
# Goal: find numbers a and b (1 to 9) where a * b == 24 and a + b == 10

print("Version 1: plain break (leaves only the inner loop)")
for a in range(1, 10):
    for b in range(1, 10):
        if a * b == 24 and a + b == 10:
            print(f"  found a={a}, b={b}")
            break                  # stops the b loop, but the a loop continues!

print("\nVersion 2: a flag also stops the outer loop")
found = False
for a in range(1, 10):
    for b in range(1, 10):
        if a * b == 24 and a + b == 10:
            print(f"  found a={a}, b={b}")
            found = True
            break                  # leave the inner loop
    if found:
        break                      # leave the outer loop too
print("  done searching")
