from typing import List


input_file = "input.txt"


def find_neighbors(i, j, h, w, matrix):
    # return 8 direction neighbors
    neighbors = []
    # right
    if j <= w - 4:
        neighbors.append(matrix[i][j:j+4]) 
    # left
    if j >= 3:
        word = matrix[i][j-3:j+1]
        neighbors.append(word[::-1])
    # down
    if i <= h - 4:
        word = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
        neighbors.append(word)
    # up
    if i >= 3:
        word = matrix[i][j] + matrix[i-1][j] + matrix[i-2][j] + matrix[i-3][j]
        neighbors.append(word)
    # up right
    if j <= w - 4 and i >= 3:
        word = matrix[i][j] + matrix[i-1][j+1] + matrix[i-2][j+2] + matrix[i-3][j+3]
        neighbors.append(word)
    # up left
    if j >= 3 and i >= 3:
        word = matrix[i][j] + matrix[i-1][j-1] + matrix[i-2][j-2] + matrix[i-3][j-3]
        neighbors.append(word)
    # down right
    if j <= w - 4 and i <= h -4:
        word = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
        neighbors.append(word)
    # down left
    if j >= 3 and i <= h - 4:
        word = matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3]
        neighbors.append(word)
    return neighbors


def find_xmas(matrix):
    h = len(matrix)
    w = len(matrix[0])
    
    found = 0
    for x in range(h):
        for y in range(w):
            cur = matrix[x][y]
            if cur == "X":
                # check
                neighbors = find_neighbors(x, y, h, w, matrix)
                found += len(list(filter(lambda s: s == "XMAS", neighbors)))
    return found


def find_mas(i, j, h, w, matrix):
    word_1 = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
    word_2 = matrix[i+1][j-1] + matrix[i][j] + matrix[i-1][j+1]
    return list(filter(lambda s: s == "SAM" or s == "MAS", [word_1, word_2]))

def find_x_mas(matrix):
    h = len(matrix)
    w = len(matrix[0])
    
    found = 0
    for x in range(1, h - 1):
        for y in range(1, w - 1):
            cur = matrix[x][y]
            if cur == "A":
                # check
                possibles = find_mas(x, y, h, w, matrix)
                if len(possibles) == 2:
                    found += 1
    return found


if __name__ == "__main__":
    data: List[str]
    with open(input_file, "r") as f:
        data = f.readlines()
    
    # print(find_xmas(data))
    print(find_x_mas(data))
