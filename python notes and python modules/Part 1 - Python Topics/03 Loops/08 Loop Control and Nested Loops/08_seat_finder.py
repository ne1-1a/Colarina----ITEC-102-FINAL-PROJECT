# Example 8 (Hard) MINI PROJECT: Exam hall seat finder
# Nested loops + continue + break + flag, all in one program.
ROWS = 5
SEATS = 6

print("=== EXAM HALL SEAT CHART ===")
print("[X] = taken   [ ] = free\n")
header = "       "
for seat in range(1, SEATS + 1):
    header += f" {seat} "
print(header)

free_seats = 0
for row in range(1, ROWS + 1):
    line = f"Row {row}: "
    for seat in range(1, SEATS + 1):
        taken = (row * seat) % 4 == 0        # a made-up rule for which seats are taken
        if taken:
            line += "[X]"
            continue                         # nothing more to do for a taken seat
        line += "[ ]"
        free_seats += 1
    print(line)

print(f"\nFree seats: {free_seats} of {ROWS * SEATS}")

# Find the FIRST free seat, scanning row by row
found = False
for row in range(1, ROWS + 1):
    for seat in range(1, SEATS + 1):
        if (row * seat) % 4 != 0:
            print(f"First free seat: Row {row}, Seat {seat}")
            found = True
            break
    if found:
        break

if not found:
    print("The hall is full!")
