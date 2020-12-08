from utils import read_input

input = read_input("day3.txt")


def find_trees(input: "list[str]", slope: "tuple[int]") -> int:
    trees = 0
    col = slope[0]
    row = slope[1]
    while row <= len(input) - 1:
        if input[row][col % len(input[0])] == "#":
            trees += 1
        col += slope[0]
        row += slope[1]
    return trees


pt1 = find_trees(input, (3, 1))
print(pt1)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
pt2 = 0
for slope in slopes:
    if pt2 == 0:
        pt2 = find_trees(input, slope)
    else:
        pt2 = pt2 * find_trees(input, slope)
print(pt2)
