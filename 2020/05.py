from utils import read_input


bps = read_input("day5.txt")

# FBFBBFFRLR
seat_ids = []
for bp in bps:
    row = 0
    min_row = 0
    max_row = 127
    for x in bp[:-3]:
        mid = (max_row - min_row) // 2
        if x == "F":
            max_row = min_row + mid
            row = max_row
        elif x == "B":
            min_row = min_row + mid + 1
            row = min_row
    min_col = 0
    max_col = 7
    col = 0
    for x in bp[7:]:
        mid = (max_col - min_col) // 2
        if x == "L":
            max_col = min_col + mid
            col = max_col
        elif x == "R":
            min_col = min_col + mid + 1
            col = min_col
    seat_ids.append((row * 8) + col)

seat_ids = sorted(seat_ids)
print(seat_ids[-1])

for idx, sid in enumerate(seat_ids):
    if idx + 1 < len(seat_ids) and sid + 1 != seat_ids[idx + 1]:
        print(sid + 1)
