# Example 8 (Hard) MINI PROJECT 3: Log file analyzer
# Streams a log file, counts the levels, copies the ERROR lines into a second file
# (two files open at the same time) and writes a report.

# --- Setup: create a sample server log ---
sample_log = """2026-11-19 08:00:01 INFO Server started
2026-11-19 08:05:13 INFO User alex logged in
2026-11-19 08:17:44 WARNING Disk usage at 85%
2026-11-19 09:02:10 ERROR Database connection failed
2026-11-19 09:02:15 INFO Retrying connection
2026-11-19 09:02:20 INFO Database connected
2026-11-19 10:30:00 WARNING Slow response: 2.4 seconds
2026-11-19 11:45:32 ERROR Payment service timeout
2026-11-19 12:00:00 INFO Backup completed
2026-11-19 13:15:09 ERROR Disk full
2026-11-19 14:00:00 INFO User sam logged in
2026-11-19 14:30:22 WARNING Memory usage at 90%
"""
with open("demo_server.log", "w") as file:
    file.write(sample_log)

# --- Pass 1: read the log and write the ERROR lines to another file ---
total = 0
info = 0
warnings = 0
errors = 0
first_time = ""
last_time = ""

with open("demo_server.log") as source, open("demo_errors.log", "w") as error_file:
    for line in source:
        line = line.strip()
        if line == "":
            continue

        total += 1
        if total == 1:
            first_time = line[:19]           # the first 19 characters are the date and time
        last_time = line[:19]

        if " INFO " in line:
            info += 1
        elif " WARNING " in line:
            warnings += 1
        elif " ERROR " in line:
            errors += 1
            error_file.write(f"Line {total}: {line}\n")    # remember WHERE the error was

# --- Pass 2: write the report using print(..., file=...) ---
with open("demo_log_report.txt", "w") as report:
    print("LOG REPORT", file=report)
    print("=" * 30, file=report)
    print(f"From        : {first_time}", file=report)
    print(f"To          : {last_time}", file=report)
    print(f"Total lines : {total}", file=report)
    print(f"INFO        : {info} ({info / total:.0%})", file=report)
    print(f"WARNING     : {warnings} ({warnings / total:.0%})", file=report)
    print(f"ERROR       : {errors} ({errors / total:.0%})", file=report)
    if errors > 2:
        print("STATUS      : ATTENTION NEEDED", file=report)
    else:
        print("STATUS      : OK", file=report)

# --- Show both new files ---
print("=== demo_log_report.txt ===")
with open("demo_log_report.txt") as file:
    for line in file:
        print(line.strip())

print("\n=== demo_errors.log ===")
with open("demo_errors.log") as file:
    for line in file:
        print(line.strip())
