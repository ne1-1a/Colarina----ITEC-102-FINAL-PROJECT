# Example 6 (Intermediate): Leap year checker - tricky logic made simple
# Rule: divisible by 4 -> leap year, EXCEPT centuries (divisible by 100),
#       unless the century is also divisible by 400.
year = int(input("Enter a year: "))

# Version 1: one long condition
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year (version 1)")
else:
    print(year, "is NOT a leap year (version 1)")

# Version 2: step by step with elif (easier to read)
if year % 400 == 0:
    result = True
elif year % 100 == 0:
    result = False
elif year % 4 == 0:
    result = True
else:
    result = False

print("Version 2 agrees?", result == ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0))
