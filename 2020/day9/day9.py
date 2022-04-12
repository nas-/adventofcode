import os

with open("input.txt") as fin:
    instructions = []
    for operation in fin:
        instructions.append(int(operation.strip()))


def check(A, number):
    for x in A:
        for y in A:
            if x + y == number and x != y:
                return True
    return False


ciptherlength = 25
found1 = False
contiguous = []
bug = 0
for instruction in range(ciptherlength, len(instructions)):
    if found1:
        break
    X = instructions[instruction]
    tocheck = instructions[instruction - ciptherlength:instruction]
    if not check(tocheck, X):
        print(f'Part 1: {X}')
        bug = X
        break

found2 = False
for instruction in range(0, len(instructions)):
    total = 0
    index = 0
    if found2:
        break
    while total < bug and index < len(instructions):
        total = sum(instructions[instruction - index:instruction])
        if total == bug:
            print(
                f'Part 2: {min(instructions[instruction - index:instruction]) + max(instructions[instruction - index:instruction])}')
            found2 = True
            break
        index = index + 1
