# Strings: Basics and Methods

## Key ideas
- A string is a sequence of characters in quotes: `"Python"` or `'Python'`.
- Strings are **immutable**: you can never change one in place, you build a **new** string.
- `len(s)` counts every character (spaces and symbols too).

## Operators
| Tool | Example | Result |
|---|---|---|
| Concatenate | `"Py" + "thon"` | `"Python"` |
| Repeat | `"ab" * 3` | `"ababab"` |
| Contains | `"Py" in "Python"` | `True` |
| f-string | `f"Hi {name}"` | inserts values |

## Indexing and slicing
```
 P  R  O  G  R  A  M        s[0] = "P"     s[-1] = "M"
 0  1  2  3  4  5  6        s[0:3] = "PRO" s[3:]  = "GRAM"
-7 -6 -5 -4 -3 -2 -1        s[::-1] = reversed
```
`s[start:stop:step]`: stop is **not** included. Slices never crash; a single index out of range does (`IndexError`).

## Methods (they RETURN a new string)
| Group | Methods |
|---|---|
| Clean | `strip()` `lstrip()` `rstrip()` |
| Case | `upper()` `lower()` `title()` `capitalize()` `swapcase()` |
| Search | `find()` (returns -1 if missing) `rfind()` `count()` `startswith()` `endswith()` |
| Replace | `replace(old, new)` |
| Check (True/False) | `isdigit()` `isalpha()` `isalnum()` `isupper()` `islower()` `isspace()` `istitle()` |
| Words | `split()` breaks text into words, `" ".join(...)` glues them back |
| Letters and numbers | `ord("a")` -> 97, `chr(97)` -> `"a"` |

## Common mistakes
1. Calling `text.upper()` and **not storing** the result.
2. Using `+` with a number (`"Age: " + 19` crashes; use `str(19)` or an f-string).
3. Counting from 1 instead of 0 when indexing.
4. `find()` returns `-1` for "not found", which is a valid-looking index in slices.
5. Trying `word[0] = "p"` (strings cannot be changed in place).

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_string_basics.py` | `len`, `+`, `*`, `in`, f-strings |
| 2 | `02_indexing_and_slicing.py` | index, negative index, slices, reverse |
| 3 | `03_string_methods.py` | strip, case, find, replace, chaining |
| 4 | `04_checking_methods.py` | `isdigit`, `isalpha`, `isalnum`... |
| 5 | `05_loop_through_strings.py` | loop characters, `ord` / `chr`, Caesar cipher |
| 6 | `06_name_formatter.py` | mini project 1: name formatter |
| 7 | `07_email_validator.py` | mini project 2: email validator |
| 8 | `08_word_statistics.py` | mini project 3: word statistics |
