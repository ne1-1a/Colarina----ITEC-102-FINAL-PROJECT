# Example 5 (Intermediate): f-strings - the modern way to format
name = "Alex"
score = 92.456
money = 1234567.891
ratio = 0.8532

print(f"Hello {name}!")
print(f"Score  : {score:.1f}")          # 1 decimal place
print(f"Money  : {money:,.2f}")         # commas + 2 decimals
print(f"Ratio  : {ratio:.1%}")          # as a percentage

# Alignment inside a width of 10
print(f"[{name:<10}]")                  # left
print(f"[{name:>10}]")                  # right
print(f"[{name:^10}]")                  # center
print(f"[{7:03d}]")                     # pad with zeros -> 007

# You can put calculations inside the braces
print(f"{5} + {3} = {5 + 3}")

# Handy for debugging (Python 3.8+)
print(f"{name = }")
