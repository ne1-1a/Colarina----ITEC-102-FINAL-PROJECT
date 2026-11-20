# Functions: Advanced

## Default arguments
```python
def greet(name, greeting="Hello"):
    ...
greet("Alex")                  # greeting = "Hello"
greet("Alex", greeting="Hi")   # keyword argument
```
- Parameters **with** defaults must come **after** those without.
- Use keyword arguments to skip some defaults (`make_label("MENU", width=30)`).

## `*args` and `**kwargs`
| Form | Collects | Inside the function |
|---|---|---|
| `*args` | any number of positional values | a group you can loop through |
| `**kwargs` | any number of `name=value` pairs | a dictionary (Data Structures topic; only a taste here) |

`add_all(*numbers)` accepts `add_all(1, 2)` or `add_all(1, 2, 3, 4, 5)`.
A `*` when **calling** unpacks a group into separate arguments.

## Returning several values
```python
def divide(a, b):
    return a // b, a % b
quotient, remainder = divide(17, 5)      # unpack into two variables
```
Without unpacking you get one packed value `(3, 2)`. Use `_` for a value you don't need.

## Recursion
A function that **calls itself**. Needs:
1. a **base case** (when to stop), and
2. a step that moves **toward** the base case.

| Problem | Base case | Recursive step |
|---|---|---|
| `factorial(n)` | `n <= 1` -> `1` | `n * factorial(n - 1)` |
| `sum_to(n)` | `n == 0` -> `0` | `n + sum_to(n - 1)` |
| `gcd(a, b)` | `b == 0` -> `a` | `gcd(b, a % b)` |

Python stops runaway recursion at about 1000 calls (`RecursionError`). Loops are usually faster, but recursion is clearer for some problems.

## lambda and functions as values
- `square = lambda x: x * x` is a tiny one-line function.
- Functions can be **passed** to other functions and **returned** from them (`apply_twice(square, 3)`, `make_multiplier(2)`).
- Handy built-ins: `max` `min` `abs` `round` `pow` `divmod` `len` `sum`.

## Common mistakes
1. Recursion **without** a base case (infinite recursion).
2. Putting a default parameter before a normal one (`SyntaxError`).
3. Forgetting to unpack a multi-value return.
4. Using `lambda` for long logic (use `def` when it needs more than one line).
5. Passing `func()` (the result) instead of `func` (the function itself).

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_default_and_keyword_arguments.py` | defaults, keyword arguments |
| 2 | `02_args_and_kwargs.py` | `*args`, bonus `**kwargs` |
| 3 | `03_return_multiple_values.py` | return and unpack several values |
| 4 | `04_recursion.py` | factorial, Fibonacci, GCD, call trace |
| 5 | `05_lambda_and_builtins.py` | lambda, functions as values, built-ins |
| 6 | `06_loan_calculator.py` | mini project 1: loan calculator |
| 7 | `07_password_checker.py` | mini project 2: password strength checker |
| 8 | `08_mini_quiz_game.py` | mini project 3: Python quiz game |
