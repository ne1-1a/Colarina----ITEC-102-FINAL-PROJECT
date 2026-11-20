# Example 4 (Intermediate): The SAME job with for and with while

# Job 1: print 1 to 5
print("for  :", end=" ")
for i in range(1, 6):
    print(i, end=" ")

print("\nwhile:", end=" ")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# Job 2: sum of 1 to 100
total_for = 0
for i in range(1, 101):
    total_for += i

total_while = 0
i = 1
while i <= 100:
    total_while += i
    i += 1
print("Both give the same sum?", total_for == total_while, "->", total_for)

# Job 3: countdown from 5
print("for   countdown:", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Job 4: a job where you do NOT know the number of repeats.
# How many times can 1000 be halved until it is below 1?
number = 1000
halvings = 0
while number >= 1:
    number //= 2
    halvings += 1
print("1000 can be halved", halvings, "times before it drops below 1")

print()
print("RULE OF THUMB:")
print("  for   -> you KNOW how many times (or what range)")
print("  while -> you repeat UNTIL something happens")
