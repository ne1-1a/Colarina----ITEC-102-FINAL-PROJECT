# match / case  (needs Python 3.10+)

## Shape
```python
match value:
    case 1:
        ...
    case "start" | "go":     # | means OR
        ...
    case _:                  # _ = anything else (default)
        ...
```
- `match` compares **one value** against many `case` options, top to bottom, and runs the **first** that fits.
- No `break` needed: only one case runs.
- `case _:` is the default. Without it, an unmatched value is silently ignored.

## What this topic covers
Values (numbers and text) | `|` (OR) | `case _` | match vs if/elif.

## When to use which?
| Use `match` | Use `if / elif` |
|---|---|
| One value, many **exact** options | Ranges (`score >= 90`) |
| Menus and commands | Conditions with `and` / `or` |
| Day numbers, directions, choices | Anything that is not a simple equality |

## Common mistakes
1. Running it on Python 3.9 or older (`SyntaxError`).
2. Forgetting `case _` for invalid input.
3. Expecting `case x > 5:` to work (it does not; use `if` for ranges).
4. Comparing text with different capitals: clean the input first with `.strip().lower()`.
5. Matching the number `1` against the text `"1"`: `input()` gives text.

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_match_numbers.py` | match with numbers |
| 2 | `02_match_strings.py` | match with text |
| 3 | `03_or_pattern.py` | `\|` OR pattern |
| 4 | `04_default_case.py` | why `case _` matters |
| 5 | `05_match_vs_if_elif.py` | same program, two styles |
| 6 | `06_menu_calculator.py` | mini project 1: menu calculator |
| 7 | `07_vending_machine.py` | mini project 2: vending machine |
| 8 | `08_text_adventure.py` | mini project 3: text adventure |
