# Operators and Type Casting

## Arithmetic
| Op | Name | `17` and `5` |
|---|---|---|
| `+` `-` `*` | add, subtract, multiply | `22`, `12`, `85` |
| `/` | division (always float) | `3.4` |
| `//` | floor division | `3` |
| `%` | modulo (remainder) | `2` |
| `**` | power | `1419857` |

**Handy uses:** `n % 2 == 0` (even?) | `minutes // 60` and `minutes % 60` (hours and minutes) | `n % 10` (last digit).

## Comparison (result is `True`/`False`)
`==` `!=` `<` `>` `<=` `>=`

## Logical
`and` (both True) | `or` (at least one True) | `not` (flip)

## Assignment shortcuts
`+=` `-=` `*=` `/=` `//=` `%=` `**=` -> `x += 5` means `x = x + 5`

## Operator order (high -> low)
`()` -> `**` -> `* / // %` -> `+ -` -> comparisons -> `not` -> `and` -> `or`
When unsure, **use parentheses**.

## Type casting
| Function | Example | Result |
|---|---|---|
| `int()` | `int("42")`, `int(9.99)` | `42`, `9` (cuts decimals) |
| `float()` | `float("3.5")` | `3.5` |
| `str()` | `str(100)` | `"100"` |
| `bool()` | `bool("")`, `bool(7)` | `False`, `True` |

## Common mistakes
1. `int("3.5")` crashes: use `int(float("3.5"))`.
2. Expecting `int()` to round (it cuts; use `round()`).
3. Writing `-2 ** 2` and expecting `4` (it is `-4`).
4. Using `=` instead of `==` in a comparison.

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_arithmetic.py` | the 7 arithmetic operators |
| 2 | `02_floor_and_modulo.py` | practical `//` and `%` |
| 3 | `03_comparison.py` | comparisons, text comparison |
| 4 | `04_logical_operators.py` | and / or / not, truth table |
| 5 | `05_assignment_operators.py` | all assignment shortcuts |
| 6 | `06_type_casting.py` | `int()`, `float()`, `str()`, `bool()` |
| 7 | `07_operator_precedence.py` | order, chained comparison, `in` |
| 8 | `08_grade_computation.py` | mini project: final grade computer |
