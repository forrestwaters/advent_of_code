def part1(arr):
    """
    Brute force - find 2 items in list that add together to be 2020
    return the product of those 2 items
    """
    for idx1 in range(0, len(arr)):
        idx2 = idx1 + 1
        if arr[idx1] > 2020:
            # could there be negative #'s?
            continue
        while idx2 <= len(arr) - 1:
            if arr[idx1] + arr[idx2] == 2020:
                print(arr[idx1] * arr[idx2])
                return
            idx2 += 1


def part2(arr):
    for idx1 in range(0, len(arr)):
        if arr[idx1] > 2020:
            continue
        for idx2 in range(idx1 + 1, len(arr) - 1):
            if arr[idx1] + arr[idx2] > 2020:
                continue
            idx3 = idx2 + 1
            while idx3 <= len(arr) - 1:
                if arr[idx1] + arr[idx2] + arr[idx3] == 2020:
                    print(arr[idx1] * arr[idx2] * arr[idx3])
                idx3 += 1


with open("day1.txt", "r") as f:
    data = [int(x.rstrip("\n")) for x in f.readlines() if x.rstrip("\n").isdigit()]

part1(data)
part2(data)
