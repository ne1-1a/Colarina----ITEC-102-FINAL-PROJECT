# Example 2 (Easy-Intermediate): Pick characters with [index] and pieces with [start:stop:step]
#   P  R  O  G  R  A  M  M  I  N  G
#   0  1  2  3  4  5  6  7  8  9  10     <- positive index (starts at 0!)
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1     <- negative index (starts from the end)
word = "PROGRAMMING"

print("First character :", word[0])
print("Second character:", word[1])
print("Last character  :", word[-1])
print("Second to last  :", word[-2])

# Slicing: word[start:stop] (stop is NOT included, just like range)
print(word[0:3])        # PRO
print(word[3:])         # from index 3 to the end
print(word[:4])         # from the start up to index 3
print(word[-4:])        # the last 4 characters
print(word[2:8])        # middle part
print(word[::2])        # every 2nd character
print(word[::-1])       # step -1 = REVERSED

# Slices are forgiving, single indexes are not
print(word[2:100])      # fine: stops at the end
# print(word[100])      # IndexError: string index out of range

# Strings are IMMUTABLE: you cannot change a character in place
# word[0] = "p"         # TypeError
changed = "p" + word[1:]     # build a NEW string instead
print(changed)
