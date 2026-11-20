# Example 8 (Hard) MINI PROJECT 3: Shopping cart with a running receipt


def get_item_name(code):
    if code == "A":
        return "Notebook"
    if code == "B":
        return "Pen"
    if code == "C":
        return "Backpack"
    if code == "D":
        return "Calculator"
    return ""                       # empty text = unknown code


def get_item_price(code):
    if code == "A":
        return 45
    if code == "B":
        return 15
    if code == "C":
        return 850
    if code == "D":
        return 600
    return 0


def apply_discount(subtotal):
    """10% off when the subtotal is PHP 1,000 or more."""
    if subtotal >= 1000:
        return subtotal * 0.90
    return subtotal


def add_vat(amount):
    return amount * 1.12


def print_line(name, price, quantity):
    print(f"  {name:<12} {quantity:>3} x {price:>7,.2f} = {price * quantity:>9,.2f}")


def main():
    print("=== SCHOOL SUPPLIES STORE ===")
    print("A Notebook   PHP 45")
    print("B Pen        PHP 15")
    print("C Backpack   PHP 850")
    print("D Calculator PHP 600")
    print("Type DONE when you are finished.\n")

    subtotal = 0

    while True:
        code = input("Item code: ").strip().upper()
        if code == "DONE":
            break

        name = get_item_name(code)
        if name == "":
            print("Unknown item code.")
            continue

        quantity = int(input("Quantity: "))
        price = get_item_price(code)
        subtotal += price * quantity
        print_line(name, price, quantity)

    discounted = apply_discount(subtotal)
    total = add_vat(discounted)

    print("\n" + "=" * 34)
    print(f"{'Subtotal':<17}: PHP {subtotal:>10,.2f}")
    print(f"{'After discount':<17}: PHP {discounted:>10,.2f}")
    print(f"{'Total (12% VAT)':<17}: PHP {total:>10,.2f}")
    print("=" * 34)


main()
