# Example 7 (Intermediate): Receipt calculator - variables doing real work

item_name = "Notebook"
price = 45.50
quantity = 4
discount_rate = 0.10      # 10%
tax_rate = 0.12           # 12% VAT

subtotal = price * quantity
discount = subtotal * discount_rate
taxable = subtotal - discount
tax = taxable * tax_rate
total = taxable + tax

print("=" * 32)
print("          RECEIPT")
print("=" * 32)
print(f"Item      : {item_name}")
print(f"Price     : PHP {price:>10.2f}")
print(f"Quantity  : {quantity:>14}")
print("-" * 32)
print(f"Subtotal  : PHP {subtotal:>10.2f}")
print(f"Discount  : PHP {discount:>10.2f}")
print(f"Tax (12%) : PHP {tax:>10.2f}")
print("-" * 32)
print(f"TOTAL     : PHP {total:>10.2f}")
print("=" * 32)
