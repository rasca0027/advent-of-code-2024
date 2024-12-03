from functools import reduce
from typing import List


input_file = "test.txt"

def is_valid_increasing(lst):
    return reduce(
        lambda acc, pair: acc and (pair[0] < pair[1]) and (pair[1] - pair[0] >= 1) and (pair[1] - pair[0] <= 3),
        zip(lst, lst[1:]),
        True
    )

def is_valid_decreasing(lst):
    return reduce(
        lambda acc, pair: acc and (pair[0] > pair[1]) and (pair[0] - pair[1] >= 1) and (pair[0] - pair[1] <= 3),
        zip(lst, lst[1:]),
        True
    )

def calculate_safe_levels(recs) -> int:
    safe_levels = 0
    for rec in recs:
        level_strings = rec.split(" ")
        levels = list(map(int, level_strings))
        if is_valid_decreasing(levels) or is_valid_increasing(levels):
            safe_levels += 1
    return safe_levels

def calculate_safe_levels_with_dampener(recs) -> int:
    safe_levels = 0
    for rec in recs:
        level_strings = rec.split(" ")
        levels = list(map(int, level_strings))
        if is_valid_decreasing(levels) or is_valid_increasing(levels):
            safe_levels += 1
        else:
            for i in range(len(levels)):
                levels_to_test = levels[:i] + levels[i + 1:]
                if is_valid_decreasing(levels_to_test) or is_valid_increasing(levels_to_test):
                    print("safe with dampener", levels)
                    safe_levels += 1
                    break

    return safe_levels


if __name__ == "__main__":
    records: List[str]
    with open(input_file, "r") as f:
        records = f.readlines()

    print(calculate_safe_levels_with_dampener(records))
