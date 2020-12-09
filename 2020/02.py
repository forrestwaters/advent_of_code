from utils import read_input

lines = read_input("day2.txt")

valid = 0
for line in lines:
    _ = line.split(":")
    count, letter = _[0].split(" ")
    min, max = count.split("-")
    pw = _[1].strip(" ")
    l_found = 0
    for char in pw:
        if char == letter:
            l_found += 1
    if l_found >= int(min) and l_found <= int(max):
        valid += 1

print(valid)

valid = 0
for line in lines:
    _ = line.split(":")
    count, letter = _[0].split(" ")
    idx1, idx2 = count.split("-")
    pw = _[1].strip(" ")
    l_found = False
    try:
        if pw[int(idx1) - 1] == letter:
            l_found = True
        if pw[int(idx2) - 1] == letter:
            l_found = not l_found
    except IndexError:
        pass
    if l_found:
        valid += 1

print(valid)
