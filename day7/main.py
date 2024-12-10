from typing import List


input_file = "input.txt"


def check_feasibility(equation, ans):
    operands = equation.lstrip().split(" ")
    operands = list(map(int, operands))
    operators = len(operands) - 1
    # res = find_possible_operators(ans, operands, operators)
    res = find_possible_operators_with_concat(ans, operands, operators)
    return res


def find_possible_operators(left, operands, operators):
    if operators == 0:
        return left == operands[0]
    plus = operands[0] + operands[1]
    multiply = operands[0] * operands[1]
    return find_possible_operators(
        left, [plus] + operands[2:], operators - 1
    ) or find_possible_operators(
        left, [multiply] + operands[2:], operators - 1
    )


def find_possible_operators_with_concat(left, operands, operators):
    if operators == 0:
        return left == operands[0]
    plus = operands[0] + operands[1]
    multiply = operands[0] * operands[1]
    concat = int(str(operands[0]) + str(operands[1]))
    return find_possible_operators_with_concat(
        left, [plus] + operands[2:], operators - 1
    ) or find_possible_operators_with_concat(
        left, [multiply] + operands[2:], operators - 1
    ) or find_possible_operators_with_concat(
        left, [concat] + operands[2:], operators - 1
    )

if __name__ == "__main__":
    data: List[str]
    with open(input_file, "r") as f:
        data = f.readlines()

    result = 0
    for line in data:
        answer, equation = line.rstrip().split(":")
        feasibility = check_feasibility(equation, int(answer))
        if feasibility:
            result += int(answer)
    print(result)
