# Input and Output

## `print()` cheat sheet
| Feature | Example | Result |
|---|---|---|
| Many items | `print("a", "b")` | `a b` |
| Separator | `print("a", "b", sep="-")` | `a-b` |
| End | `print("Hi", end="!")` | stays on the same line |
| New line / tab | `"\n"`, `"\t"` | line break / tab |
| Quote / backslash | `\"`, `\'`, `\\` | shows the character |
| Raw string | `r"C:\new"` | backslashes untouched |

## `input()`
- Shows a message, waits for the user, and returns **text (`str`)**, always.
- Convert when you need numbers: `int(input(...))`, `float(input(...))`.

## f-strings (`f"..."`)
| Format | Meaning | Example -> result |
|---|---|---|
| `{x}` | insert a value | `f"Hi {name}"` |
| `{x:.2f}` | 2 decimals | `3.14159` -> `3.14` |
| `{x:,}` | thousands commas | `1000000` -> `1,000,000` |
| `{x:.1%}` | percentage | `0.853` -> `85.3%` |
| `{x:<10}` `{x:>10}` `{x:^10}` | left / right / center in 10 spaces | |
| `{x:03d}` | pad with zeros | `7` -> `007` |

## Common mistakes
1. Doing math on `input()` without converting (`"5" + "3"` is `"53"`).
2. Typing letters when `int()` expects digits -> `ValueError` (the exception-handling topic fixes this).
3. Forgetting the `f` before the quotes.

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_print_basics.py` | print, `sep`, `end` |
| 2 | `02_print_formatting.py` | escapes, raw strings, decorating |
| 3 | `03_first_input.py` | first `input()` |
| 4 | `04_input_numbers.py` | `input()` + `int()` / `float()` |
| 5 | `05_fstrings.py` | f-string formatting |
| 6 | `06_age_calculator.py` | input + math |
| 7 | `07_bill_splitter.py` | input + formatted money |
| 8 | `08_mini_form.py` | mini project: registration card |
