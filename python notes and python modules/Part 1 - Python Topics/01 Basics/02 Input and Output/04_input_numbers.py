# Example 4 (Easy-Intermediate): input() always returns TEXT
first = input("First number : ")
second = input("Second number: ")

# Without converting, + glues the TEXT together
print("Without converting:", first + second)      # "5" + "3" = "53"

# int() and float() turn text into numbers
a = int(first)
b = int(second)
print("After converting  :", a + b)

price = float(input("Price of one item (PHP): "))
quantity = int(input("How many? "))
print("Total:", price * quantity)
