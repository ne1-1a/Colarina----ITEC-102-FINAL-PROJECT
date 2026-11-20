# Example 5 (Intermediate): The SAME program with if/elif and with match
size = input("Coffee size (small / medium / large): ").strip().lower()

# --- Version 1: if / elif ---
if size == "small":
    price_1 = 60
elif size == "medium":
    price_1 = 80
elif size == "large":
    price_1 = 100
else:
    price_1 = 0

# --- Version 2: match / case ---
match size:
    case "small":
        price_2 = 60
    case "medium":
        price_2 = 80
    case "large":
        price_2 = 100
    case _:
        price_2 = 0

print("if/elif price   :", price_1)
print("match price     :", price_2)
print("Same answer?    :", price_1 == price_2)

# When to use which?
#   match   -> ONE value compared against MANY exact options (menus, commands)
#   if/elif -> ranges (score >= 90) or conditions with and / or
