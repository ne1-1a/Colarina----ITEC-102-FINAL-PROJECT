# Example 7 (Intermediate-Hard): Which operator goes first?
# Order (high to low): ()  **  * / // %  + -  comparisons  not  and  or

print(2 + 3 * 4)          # 14: multiply first
print((2 + 3) * 4)        # 20: parentheses first
print(2 ** 3 ** 2)        # 512: power goes right to left (3**2 = 9, then 2**9)
print(-2 ** 2)            # -4: power before the minus sign
print(10 - 2 - 3)         # 5: left to right
print(100 / 10 * 2)       # 20.0: left to right

# Comparisons run after math
print(2 + 3 > 4)          # True

# Chained comparison - Python can read it like math class
x = 5
print(1 < x < 10)         # True

# "in" checks if text is inside other text
print("py" in "python")
print("z" in "python")
print("z" not in "python")

# and runs before or. Parentheses make your meaning clear.
age = 20
print(age > 18 and age < 30 or age == 5)
print(age > 18 and (age < 15 or age == 20))
