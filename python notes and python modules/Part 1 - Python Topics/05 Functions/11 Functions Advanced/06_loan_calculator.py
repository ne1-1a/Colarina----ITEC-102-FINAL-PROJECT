# Example 6 (Hard) MINI PROJECT 1: Loan calculator (default arguments in action)


def monthly_payment(principal, annual_rate=0.06, years=5):
    """Monthly payment for a loan using the standard amortization formula."""
    months = years * 12
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        return principal / months
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


def total_interest(principal, annual_rate=0.06, years=5):
    total_paid = monthly_payment(principal, annual_rate, years) * years * 12
    return total_paid - principal


def print_summary(principal, annual_rate=0.06, years=5):
    payment = monthly_payment(principal, annual_rate, years)
    interest = total_interest(principal, annual_rate, years)
    print(f"Loan PHP {principal:,.0f} | {annual_rate:.1%} for {years} year(s)")
    print(f"  Monthly payment : PHP {payment:,.2f}")
    print(f"  Total interest  : PHP {interest:,.2f}")


print("=== LOAN CALCULATOR ===")
amount = float(input("Loan amount (PHP): "))

print()
print_summary(amount)                      # all defaults: 6%, 5 years
print_summary(amount, years=3)             # shorter loan
print_summary(amount, 0.08, 2)             # higher rate, even shorter

print("\nHow the number of years changes the monthly payment (6% rate):")
for years in range(1, 6):
    print(f"  {years} year(s): PHP {monthly_payment(amount, years=years):>12,.2f} per month")
