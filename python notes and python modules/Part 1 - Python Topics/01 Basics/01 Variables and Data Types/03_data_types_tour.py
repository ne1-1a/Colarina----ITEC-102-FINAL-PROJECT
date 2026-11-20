# Example 3 (Easy): The basic data types
whole_number = 42          # int
decimal = 3.14             # float
text = "Hello"             # str
truth = True               # bool
nothing = None             # NoneType

print(whole_number, "->", type(whole_number).__name__)
print(decimal, "->", type(decimal).__name__)
print(text, "->", type(text).__name__)
print(truth, "->", type(truth).__name__)
print(nothing, "->", type(nothing).__name__)

# 5 and 5.0 look alike but are different types
print(type(5).__name__, type(5.0).__name__)

# isinstance() answers: "is this value of that type?"
print(isinstance(whole_number, int))
print(isinstance(whole_number, float))

# Strings can use single, double or triple quotes
single = 'It works'
double = "It also works"
multi = """Triple quotes can
hold many lines"""
print(single, "|", double)
print(multi)
