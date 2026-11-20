# Example 6 (Intermediate): True, False, "falsy" values and None

is_raining = True
has_umbrella = False
print(is_raining, has_umbrella)

# Comparisons create booleans, so you can store them
age = 17
can_vote = age >= 18
print("Can vote?", can_vote)

# bool() shows what Python considers False ("falsy") or True ("truthy")
print("Falsy :", bool(0), bool(0.0), bool(""), bool(None))
print("Truthy:", bool(1), bool(-5), bool("hi"), bool(" "))

# None means "no value yet"
middle_name = None
print("No middle name yet?", middle_name is None)
middle_name = "Lee"
print("No middle name yet?", middle_name is None)

# Behind the scenes: True is 1 and False is 0
print(True + True)
print(False + 5)
