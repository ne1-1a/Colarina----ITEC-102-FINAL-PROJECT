# Loop Control and Nested Loops

## The loop-control statements
| Statement | What it does | Works in |
|---|---|---|
| `break` | Leave the loop **immediately** | `for`, `while` |
| `continue` | Skip the **rest of this round**, go to the next | `for`, `while` |
| `pass` | Do nothing (a placeholder so the code is valid) | anywhere |
| `else` on a loop | Runs only if the loop finished **without** `break` | `for`, `while` |

### Loop `else` in one picture
```python
for divisor in range(2, number):
    if number % divisor == 0:
        break            # found one -> else is SKIPPED
else:
    print("prime")       # no break happened -> else RUNS
```

## Nested loops
- A loop inside another loop. The **inner loop runs fully** for every step of the outer loop.
- Total steps = outer repeats x inner repeats.
- Typical uses: tables and grids (rows x columns), patterns, checking pairs, searching.
- Use `print(..., end="")` to stay on the same line, and a bare `print()` after the inner loop to start a new row.

## break inside nested loops
`break` only leaves the **innermost** loop. To stop both:
```python
found = False
for a in range(...):
    for b in range(...):
        if condition:
            found = True
            break      # leaves the inner loop
    if found:
        break          # leaves the outer loop
```

## Common mistakes
1. Expecting `break` to stop the outer loop too.
2. `continue` in a `while` loop **before** updating the counter -> infinite loop.
3. Mixing up which variable (row or column) belongs to which loop.
4. Forgetting `print()` after the inner loop, so every row ends up on one line.
5. Deeply nested loops (3+) get slow and hard to read; look for a simpler way.

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_break.py` | `break` in `for` and `while` |
| 2 | `02_continue.py` | `continue`, and the while pitfall |
| 3 | `03_pass_and_loop_else.py` | `pass`, `for/else`, `while/else` |
| 4 | `04_nested_loops_basics.py` | loop inside a loop, multiplication table |
| 5 | `05_nested_patterns.py` | rectangle, hollow box, triangle, checkerboard |
| 6 | `06_break_in_nested_loops.py` | break and the "found" flag |
| 7 | `07_prime_finder.py` | nested loops + `break` + `for/else` |
| 8 | `08_seat_finder.py` | mini project: exam hall seat finder |
