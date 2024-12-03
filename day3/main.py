from typing import List
import re


input_file = "input.txt"


def calculate_muliply_answers(program):
    captures = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", program)

    result = 0
    for a, b in captures:
        # tuple of 'a', 'b'
        result += int(a) * int(b)
    return result


def calculate_muliply_answers_with_condition(program):
    captures = re.findall(r"(mul\((\d{1,3})\,(\d{1,3})\))|(do(n't)?\(\))", program)
    # [('mul(2,4)', '2', '4', '', ''), ('', '', '', "don't", "n't"), ('', '', '', 'do', ''), ('mul(8,5)', '8', '5', '', '')]
    
    answer = 0
    enabled = True
    for capture in captures:
        if capture[3] == "do()":
            enabled = True
        elif capture[3] == "don't()":
            enabled = False
        else:
            if enabled:
                print("add")
                answer += int(capture[1]) * int(capture[2])
            else:
                print("skip")
    return answer


if __name__ == "__main__":
    records: List[str]
    with open(input_file, "r") as f:
        data = f.readlines()

    print(calculate_muliply_answers_with_condition(''.join(data)))
