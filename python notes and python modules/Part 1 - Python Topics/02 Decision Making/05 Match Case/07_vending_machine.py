# Example 7 (Hard) MINI PROJECT 2: Vending machine
print("=== VENDING MACHINE ===")
print("A1  Chips   PHP 25")
print("A2  Soda    PHP 30")
print("B1  Cookie  PHP 20")
print("B2  Water   PHP 15")

money = float(input("\nInsert money (PHP): "))
code = input("Enter item code: ").strip().upper()

item = None          # None = nothing chosen yet
price = 0

match code:
    case "A1":
        item = "Chips"
        price = 25
    case "A2":
        item = "Soda"
        price = 30
    case "B1":
        item = "Cookie"
        price = 20
    case "B2":
        item = "Water"
        price = 15
    case _:
        print("Invalid code. Your money is returned.")

if item is not None:
    if money < price:
        print(f"Not enough money. {item} costs PHP {price}, you inserted PHP {money:.2f}.")
    else:
        change = money - price
        print(f"Here is your {item}!")
        if change > 0:
            print(f"Your change: PHP {change:.2f}")
