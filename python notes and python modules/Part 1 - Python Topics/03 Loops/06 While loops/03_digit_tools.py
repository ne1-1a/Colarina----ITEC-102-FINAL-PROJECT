# Example 3 (Intermediate): Take a number apart, one digit at a time
number = int(input("Enter a positive whole number: "))
original = number

digit_count = 0
digit_sum = 0
reversed_number = 0

while number > 0:
    last_digit = number % 10                          # grab the last digit
    digit_sum += last_digit
    reversed_number = reversed_number * 10 + last_digit
    digit_count += 1
    number //= 10                                     # drop the last digit

print(f"Digits         : {digit_count}")
print(f"Sum of digits  : {digit_sum}")
print(f"Reversed       : {reversed_number}")
print(f"Palindrome?    : {original == reversed_number}")
