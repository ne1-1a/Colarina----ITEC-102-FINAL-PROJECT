# while Loops

## Shape
```python
count = 1                 # 1. START value
while count <= 5:         # 2. CONDITION (checked before every round)
    print(count)
    count += 1            # 3. CHANGE (so the condition can become False)
```
A `while` loop repeats **as long as its condition is True**. Use it when you do **not** know in advance how many repeats you need.

## Common patterns
| Pattern | Idea | Example file |
|---|---|---|
| Counter | count up or down | `01`, `02` |
| Accumulator | keep a running total / product | `02` |
| Digit loop | `n % 10` grabs a digit, `n //= 10` drops it | `03` |
| Validation loop | ask again until the input is valid | `04` |
| `while True` + `break` | loop forever, leave when something happens | `05` |
| Sentinel loop | a special value (like `0`) means "stop" | `05`, `08` |
| Flag loop | `while running:` and set `running = False` | `07` |

## Infinite loops
- Happens when the condition never becomes False (you forgot the change step).
- Stop a runaway program with **Ctrl + C**.
- Intentional infinite loops (`while True`) **must** have a `break` (or `return`).

## Common mistakes
1. Forgetting to update the variable in the condition.
2. Off-by-one: `<` vs `<=`.
3. Using `=` instead of `==` in the condition.
4. Converting input with `int()` before checking it is a number (crashes on letters, so check with `.isdigit()` first).

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_basic_while.py` | the 3 parts of a while loop |
| 2 | `02_countdown_and_sum.py` | countdown, accumulators, unknown repeats |
| 3 | `03_digit_tools.py` | digit sum, reverse, palindrome |
| 4 | `04_input_validation.py` | ask until valid |
| 5 | `05_while_true_and_sentinel.py` | `while True`, `break`, sentinel |
| 6 | `06_guessing_game.py` | mini project 1: number guessing game |
| 7 | `07_atm_menu.py` | mini project 2: ATM menu system |
| 8 | `08_number_analyzer.py` | mini project 3: number analyzer |
