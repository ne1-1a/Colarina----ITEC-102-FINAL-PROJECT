# Variables and Data Types

## Key ideas
- A **variable** is a name that points to a value: `age = 19`.
- `=` **stores** a value (it is not "equals" like in math).
- Python figures out the type by itself (no need to declare it).

## The basic data types
| Type | Example | Used for |
|---|---|---|
| `int` | `42` | whole numbers |
| `float` | `3.14` | decimal numbers |
| `str` | `"Hello"` | text |
| `bool` | `True` / `False` | yes/no answers |
| `NoneType` | `None` | "no value yet" |

## Naming rules
- Start with a letter or `_`; then letters, digits or `_`.
- No spaces, no dashes, no Python keywords (`class`, `if`, `for`...).
- **Case-sensitive:** `score` and `Score` are different.
- Style: `snake_case` for variables, `UPPER_CASE` for constants.

## Useful tools
`type(x)` shows the type | `isinstance(x, int)` checks it | `del x` removes it | `bool(x)` shows if a value is truthy or falsy.

## Common mistakes
1. Using `=` when you mean `==`.
2. Starting a name with a number (`2nd = 5`).
3. Trusting `0.1 + 0.2 == 0.3` (it is `False`; decimals are not exact).
4. Using a variable before giving it a value (`NameError`).

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_first_variables.py` | create variables, `type()` |
| 2 | `02_naming_rules.py` | naming, case-sensitivity, swap |
| 3 | `03_data_types_tour.py` | int/float/str/bool/None, `isinstance` |
| 4 | `04_changing_values.py` | reassign, `+=`, constants, `del` |
| 5 | `05_numbers_big_and_small.py` | big ints, float precision, rounding |
| 6 | `06_boolean_and_none.py` | truthy/falsy, `None` |
| 7 | `07_receipt_calculator.py` | variables in real calculations |
| 8 | `08_student_profile_card.py` | mini project: profile card |
