# Example 1 (Easy-Intermediate): Default values and keyword arguments


def greet(name, greeting="Hello"):          # greeting has a DEFAULT value
    print(f"{greeting}, {name}!")


greet("Alex")                               # uses the default
greet("Alex", "Good morning")               # overrides it
greet("Sam", greeting="Hey")                # keyword argument


def power(base, exponent=2):
    return base ** exponent


print(power(5))          # 25 (default exponent)
print(power(2, 10))      # 1024


def make_label(text, symbol="*", width=20):
    print(symbol * width)
    print(text.center(width))
    print(symbol * width)


make_label("MENU")
make_label("MENU", width=30)                # skip symbol, change only width
make_label("MENU", "=", 10)


def final_price(price, discount=0.0, tax=0.12):
    return price * (1 - discount) * (1 + tax)


print(f"{final_price(100):.2f}")                    # tax only
print(f"{final_price(100, discount=0.10):.2f}")     # 10% discount
print(f"{final_price(100, tax=0):.2f}")             # no tax

# RULE: parameters WITH defaults must come AFTER those without
# def bad(a=1, b):      # SyntaxError
