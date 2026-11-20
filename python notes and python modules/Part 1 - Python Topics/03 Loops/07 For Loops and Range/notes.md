# for Loops and range()

## Shape
```python
for i in range(1, 6):     # i takes the values 1, 2, 3, 4, 5
    print(i)
```
A `for` loop repeats **a known number of times**. `range()` produces the numbers to loop over.

## The three forms of range()
| Form | Produces | Example |
|---|---|---|
| `range(stop)` | `0` up to `stop - 1` | `range(5)` -> 0 1 2 3 4 |
| `range(start, stop)` | `start` up to `stop - 1` | `range(1, 6)` -> 1 2 3 4 5 |
| `range(start, stop, step)` | jump by `step` | `range(2, 11, 2)` -> 2 4 6 8 10 |

**The stop value is NEVER included.** To include `n`, write `range(1, n + 1)`.
Count down with a negative step: `range(10, 0, -1)`.

## for vs while
| Use `for` + `range` | Use `while` |
|---|---|
| You know how many times | You repeat **until something happens** |
| Counting, totals, tables, patterns | Validation, menus, games, digit loops |

## Handy patterns
- Repeat N times: `for _ in range(N):`
- Running total: `total += i`
- Table of results: `print(f"{n} x {i} = {n * i}")`
- Text patterns: `"*" * i` repeats a symbol `i` times

## Common mistakes
1. Off-by-one: `range(1, 10)` stops at 9.
2. Counting down without a negative step (`range(10, 0)` is empty).
3. Changing the loop variable inside the loop and expecting it to change the next round (it resets each round).
4. Forgetting `int()` around `input()` before using it in `range()`.

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_range_basics.py` | `range(stop)`, `(start, stop)`, `(start, stop, step)` |
| 2 | `02_range_steps.py` | steps, negative steps, empty ranges |
| 3 | `03_accumulators.py` | sums, factorial, counters |
| 4 | `04_for_vs_while.py` | same job both ways, when to use which |
| 5 | `05_range_with_math.py` | squares, powers, conversion table, FizzBuzz |
| 6 | `06_multiplication_table_generator.py` | mini project 1: table generator |
| 7 | `07_grade_calculator.py` | mini project 2: grade calculator |
| 8 | `08_pattern_printer.py` | mini project 3: pattern printer |
