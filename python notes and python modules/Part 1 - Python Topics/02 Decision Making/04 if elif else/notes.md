# if / elif / else

## Shape
```python
if condition_1:
    ...            # runs if condition_1 is True
elif condition_2:
    ...            # runs if condition_1 is False and condition_2 is True
else:
    ...            # runs if everything above is False
```
- Python checks **top to bottom** and stops at the **first** True condition.
- The code that belongs to a branch is **indented** (4 spaces) and the line ends with `:`.
- `elif` and `else` are optional. You can have many `elif`s but only one `else`.

## Tools you will combine with it
- Comparisons: `==  !=  <  >  <=  >=`
- Logic: `and`, `or`, `not` (use parentheses when mixing)
- Nested `if`: a decision inside a decision

## Tips
- Put the **most specific / highest** condition first (`score >= 90` before `score >= 80`).
- Store a True/False answer in a variable: `is_student = answer == "yes"`.
- Prefer `elif` over many separate `if`s when only ONE branch should run.

## Common mistakes
1. Forgetting the `:` at the end of the line.
2. Wrong indentation (`IndentationError`).
3. `if x = 5` (assignment) instead of `if x == 5`.
4. Wrong order of `elif` conditions, so the first one swallows everything.
5. Comparing text with different capitals (`"Yes" != "yes"`; use `.lower()`).

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_simple_if.py` | single `if` |
| 2 | `02_if_else.py` | two paths |
| 3 | `03_if_elif_else.py` | many paths: grade letter |
| 4 | `04_logical_conditions.py` | `and` / `or` / `not` |
| 5 | `05_nested_if.py` | login with nested decisions |
| 6 | `06_leap_year.py` | tricky logic, two versions |
| 7 | `07_ticket_price.py` | groups + extra discounts |
| 8 | `08_electricity_bill.py` | mini project: tiered rates |
