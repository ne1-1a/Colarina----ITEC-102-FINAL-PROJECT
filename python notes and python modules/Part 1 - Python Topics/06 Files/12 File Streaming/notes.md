# File Streaming (reading and writing text files)

## Why files?
Variables disappear when the program ends. **Files keep data** between runs: diaries, high scores, grade books, logs.

## The basic recipe
```python
with open("notes.txt", "r") as file:     # open, do the work, close automatically
    for line in file:                    # stream it, one line at a time
        print(line.strip())
```

## File modes
| Mode | Meaning | If the file exists | If it does not exist |
|---|---|---|---|
| `"r"` | read (default) | reads it | **crashes** (`FileNotFoundError`) |
| `"w"` | write | **ERASES it**, starts fresh | creates it |
| `"a"` | append | keeps it, adds to the end | creates it |

## Reading tools
| Tool | What you get |
|---|---|
| `file.read()` | the **whole** file as one string |
| `file.read(n)` | the next `n` characters |
| `file.readline()` | the next single line (with its `\n`), or `""` at the end |
| `for line in file:` | **streaming**: one line per round, only one line in memory |

**Streaming** means the program never loads the whole file at once, so it works on huge files too. `readlines()` returns a list of every line, which loads everything and needs the Data Structures topic, so it is not used here.

## Writing tools
| Tool | Notes |
|---|---|
| `file.write(text)` | text only (convert numbers with `str()`), does **not** add `\n` |
| `print(text, file=file)` | works like `print`, adds the `\n` for you |

## Handy details
- Every line read from a file ends with `\n`. Remove it with `line.strip()`.
- Everything in a file is **text**: convert with `int()` / `float()` when you read numbers.
- `with` closes the file automatically (`file.closed` becomes `True`). Always prefer it over `open()` + `close()`.
- Check a file exists before reading it: `os.path.exists("name.txt")` (the `os` module is covered in Part 2).
- Saving names with special letters (like n with a tilde): use `open(name, mode, encoding="utf-8")`.
- Relative file names live in the folder **you run the program from**. Run `python file.py` from inside the topic folder.
- Storing `name,grade` per line is a tiny "database". Split at the comma with `find()` / `rfind()` and slicing.

## Common mistakes
1. Opening with `"w"` when you meant `"a"`: **you erased your data**.
2. Forgetting `\n` between `write()` calls (everything ends up on one line).
3. `file.write(42)` fails; use `file.write(str(42))`.
4. Reading a file that does not exist yet.
5. Reading the file twice with the same open file (the second `read()` returns `""` because you are already at the end).
6. Not closing the file (use `with`).

## Files created by these examples
The examples create `demo_*.txt` / `.log` files plus `diary.txt` and `gradebook.txt` in the folder you run them from. Open them to see the results. They are ignored by Git, and you can delete them any time.

## Examples (easy -> hard)
| # | File | Skill |
|---|---|---|
| 1 | `01_write_a_file.py` | `open(..., "w")`, `write`, `close`, `print(file=)` |
| 2 | `02_read_with_with.py` | `with`, `read()`, `read(n)`, `readline()` |
| 3 | `03_streaming_line_by_line.py` | `for line in file`, numbering, statistics, search |
| 4 | `04_append_and_modes.py` | `"w"` vs `"a"` vs `"r"` |
| 5 | `05_save_and_load_numbers.py` | saving numbers, `os.path.exists`, high-score saver |
| 6 | `06_diary_app.py` | mini project 1: diary that remembers |
| 7 | `07_grade_book.py` | mini project 2: grade book (`name,grade` lines) |
| 8 | `08_log_analyzer.py` | mini project 3: log analyzer, two files at once |
