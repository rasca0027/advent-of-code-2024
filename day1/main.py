from collections import defaultdict
from typing import List


def calculate_distance(list_a, list_b) -> int:
    sorted_a = sorted(list_a)
    sorted_b = sorted(list_b)
    diff = 0
    for i, loc in enumerate(sorted_a):
        diff += abs(sorted_a[i] - sorted_b[i])
    return diff


def calculate_similarity_score(list_a, list_b) -> int:
    appearence = defaultdict(int)
    for b in list_b:
        appearence[b] += 1

    score = 0
    for a in list_a:
        score += appearence[a] * a
    return score


if __name__ == "__main__":
    data: List[str]
    with open("input.txt", "r") as f:
        data = f.readlines()

    left = []
    right = []
    for location in data:
        l, r = location.split("   ")
        left.append(int(l))
        right.append(int(r))

    # print(calculate_distance(left, right))
    print(calculate_similarity_score(left, right))
