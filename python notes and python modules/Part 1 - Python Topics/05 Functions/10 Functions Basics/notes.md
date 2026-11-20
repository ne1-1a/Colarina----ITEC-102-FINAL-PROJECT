# Functions: Basics

## Why functions?
Write code **once**, reuse it many times, give it a **name**, and break big programs into small, testable pieces.

## Shape
```python
def add(a, b):              # def + name + (parameters) + :
    """Return a + b."""     # docstring (optional, explains the function)
    return a + b            # body is indented

result = add(3, 4)          # CALL it with arguments
```

## Vocabulary
| Word | Meaning |
|---|---|
| **parameter** | the name in the `def` line (`a`, `b`) |
| **argument** | the value you pass when calling (`3`, `4`) |
| **return value** | what the function hands back with `return` |
| **call** | running the function with `name(...)` |

## `print` vs `return`
| | `print()` | `return` |
|---|---|---|
| Purpose | **show** something | **hand back** a value |
| Can you reuse the result? | No | Yes: `x = square(5)` |
| If a function has no `return` | it gives back `None` | |

`return` also **ends the function immediately**, so code after it is skipped.

## Scope
- Variables created **inside** a function are **local** (they disappear after it ends).
- A function can **read** global variables, but to change one it needs `global` (avoid this).
- **Best habit:** pass values in as parameters, send results out with `return`.

## Good function habits
- One function = one job, with a clear verb name (`calculate_total`, `is_prime`).
- Define functions **before** the code that calls them.
- Keep the menu and loop in `main()` and the logic in small functions.

## Common mistakes
1. Forgetting the parentheses when calling (`greet` instead of `greet()`).
2. Using `print` inside when the caller needs a `return`.
3. Calling a function before defining it.
4. Expecting a changed parameter to change the caller's variable.
5. Wrong number of arguments (`TypeError`).

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_define_and_call.py` | `def`, calling, docstring |
| 2 | `02_parameters.py` | parameters, positional vs keyword arguments |
| 3 | `03_return_values.py` | `return`, `print` vs `return`, early return |
| 4 | `04_functions_calling_functions.py` | small functions working together |
| 5 | `05_variable_scope.py` | local vs global, `global`, shadowing |
| 6 | `06_temperature_converter.py` | mini project 1: converter with a menu |
| 7 | `07_number_toolkit.py` | mini project 2: number toolkit |
| 8 | `08_shopping_cart.py` | mini project 3: shopping cart with receipt |
