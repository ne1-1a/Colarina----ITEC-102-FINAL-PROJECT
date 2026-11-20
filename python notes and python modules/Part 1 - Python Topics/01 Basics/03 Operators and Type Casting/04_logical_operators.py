# Example 4 (Intermediate): and, or, not
age = 20
has_id = True

print("age >= 18 and has_id  :", age >= 18 and has_id)
print("age < 13 or age > 60  :", age < 13 or age > 60)
print("not has_id            :", not has_id)

# Truth table: every possible combination
print()
print("True  and True  =", True and True)
print("True  and False =", True and False)
print("False and False =", False and False)
print("True  or  False =", True or False)
print("False or  False =", False or False)
print("not True        =", not True)
print("not False       =", not False)

# Real-life rule: can enter the concert?
has_ticket = True
is_banned = False
print("Can enter?", has_ticket and not is_banned)
