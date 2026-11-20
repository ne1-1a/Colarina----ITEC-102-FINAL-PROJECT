# Example 8 (Hard): Electricity bill with tiered rates (sample rates, not real ones)
#   first 100 kWh   -> PHP 8 per kWh
#   next 200 kWh    -> PHP 10 per kWh
#   above 300 kWh   -> PHP 12 per kWh
#   plus 12% VAT, and a PHP 50 discount for senior citizens
kwh = float(input("Electricity used this month (kWh): "))
is_senior = input("Senior citizen? (yes/no): ").lower() == "yes"

if kwh < 0:
    print("kWh cannot be negative.")
else:
    if kwh <= 100:
        charge = kwh * 8
    elif kwh <= 300:
        charge = 100 * 8 + (kwh - 100) * 10
    else:
        charge = 100 * 8 + 200 * 10 + (kwh - 300) * 12

    vat = charge * 0.12
    total = charge + vat

    if is_senior:
        total = total - 50
        if total < 0:
            total = 0

    print()
    print(f"Energy charge : PHP {charge:>10,.2f}")
    print(f"VAT (12%)     : PHP {vat:>10,.2f}")
    if is_senior:
        print(f"Senior disc.  : PHP {-50:>10,.2f}")
    print("-" * 30)
    print(f"TOTAL BILL    : PHP {total:>10,.2f}")

    if kwh > 300:
        print("Tip: you are in the highest tier. Try to save energy!")
