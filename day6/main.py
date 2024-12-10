from collections import defaultdict
import copy
from typing import List


input_file = "input.txt"
directions = {
    "^": "up",
    ">": "right",
    "<": "left",
    "v": "down",
}


def going_outside(x, y, d, w, h):
    return (d == "up" and x == 0) or (
        d == "right" and y == w - 1) or (
        d == "down" and x == h - 1) or (
        d == "left" and y == 0)


def calculate_distinct_positions(matrix, x, y, d, w, h):

    while True:
        matrix[x][y] = "X"

        if going_outside(x, y, d, w, h):
            print("leaving")
            break

        print("not leaving")

        if d == "up":
            if matrix[x - 1][y] == "#":
                d = "right"
            else:
                x -= 1
        elif d == "right":
            if matrix[x][y + 1] == "#":
                d = "down"
            else:
                y += 1
        elif d == "down":
            if matrix[x + 1][y] == "#":
                d = "left"
            else:
                x += 1
        else:  # left
            if matrix[x][y - 1] == "#":
                d = "up"
            else:
                y -= 1

    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "X":
                count += 1

    return count


def has_loop_with_obstacle(matrix, x, y, d, w, h, obstacle_x, obstacle_y):
    print("in :trying", obstacle_x, obstacle_y, d)
    print(f"x{x} y{y} w{w} h{h}")
    if matrix[obstacle_x][obstacle_y] != ".":
        return False

    matrix[obstacle_x][obstacle_y] = "#"

    trails = [[[] for i in range(w)] for j in range(h)] 

    while True:


        matrix[x][y] = "X"
        if d in trails[x][y]:
            return True
        trails[x][y].append(d)

        # print(x, y, d, trails[x][y])

        if going_outside(x, y, d, w, h):
            print("leaving")
            return False

        if d == "up":
            if matrix[x - 1][y] == "#":
                d = "right"
            else:
                x -= 1
        elif d == "right":
            if matrix[x][y + 1] == "#":
                d = "down"
            else:
                y += 1
        elif d == "down":
            if matrix[x + 1][y] == "#":
                d = "left"
            else:
                x += 1
        else:  # left
            if matrix[x][y - 1] == "#":
                d = "up"
            else:
                y -= 1




if __name__ == "__main__":
    data: List[str]
    with open(input_file, "r") as f:
        data = f.readlines()

    h = len(data)
    w = len(data[0].rstrip())

    start_x = None
    start_y = None
    original_matrix = []
    for x in range(h):
        for y in range(w):
            if data[x][y] in directions:
                # found start pos
                start_x = x
                start_y = y
                direction = directions[data[x][y]]
        original_matrix.append(list(data[x].rstrip()))
    # print(calculate_distinct_positions(original_matrix, start_x, start_y, direction, w, h))

    # print(has_loop_with_obstacle(original_matrix, start_x, start_y, "up", w, h, 6, 3))

    possible_obstacles = 0
    for obstacle_x in range(h):
        for obstacle_y in range(w):
            print("trying", obstacle_x, obstacle_y, direction)
            matrix = copy.deepcopy(original_matrix)
            if has_loop_with_obstacle(
                matrix, start_x, start_y, direction, w, h, obstacle_x, obstacle_y
            ):
                print("loop", obstacle_x, obstacle_y)
                possible_obstacles += 1
            else:
                print("no loop", obstacle_x, obstacle_y, "\n")
    print(possible_obstacles)
