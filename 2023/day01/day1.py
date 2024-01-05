from pathlib import Path
import re
from copy import deepcopy

inputs = Path("input").read_text().strip()

cleaned = ["".join(filter(lambda x: x.isdigit(), list(x))) for x in inputs.split("\n")]
result_part_1 = sum([int(str(x)[0] + str(x)[-1]) for x in cleaned])
print(f"{result_part_1= }")

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def clean_line(line_in):
    while line:
        if line_in[0].isdecimal():
            return line_in[0]
        for x, replacement in replacements.items():
            if line_in.startswith(x):
                return replacement
        line_in = line_in[1:]


def clean_line_end(line_in):
    while line:
        if line_in[-1].isdecimal():
            return line_in[-1]
        for x, replacement in replacements.items():
            if line_in.endswith(x):
                return replacement
        line_in = line_in[:-1]


result_part_2 = 0
for line in inputs.splitlines():
    first_number = clean_line(deepcopy(line))
    second_number = clean_line_end(line)
    result_part_2 += int(first_number + second_number)
print(f"{result_part_2= }")
