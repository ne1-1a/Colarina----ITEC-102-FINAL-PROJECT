# Example 5 (Intermediate): Working with big, small and decimal numbers

big = 1_000_000_000          # underscores make big numbers readable
print(big)
print(f"{big:,}")            # show with commas

huge = 2 ** 100              # Python ints can be as big as memory allows
print("2 to the power of 100:", huge)

# Decimals are not always exact (computers store them in binary)
print(0.1 + 0.2)                         # 0.30000000000000004
print(round(0.1 + 0.2, 2))               # 0.3
print(abs((0.1 + 0.2) - 0.3) < 1e-9)     # the safe way to compare decimals

# Scientific notation
print(1.5e3)       # 1500.0
print(2e-3)        # 0.002

# Division always gives a float, floor division keeps an int
print(10 / 2, type(10 / 2).__name__)
print(10 // 2, type(10 // 2).__name__)

# round(): Python rounds .5 to the nearest EVEN number
print(round(3.14159, 2))
print(round(2.5), round(3.5))
