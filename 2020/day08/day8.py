with open("input.txt") as fin:
    instructions = [
        (operation, int(argument)) for operation, argument in map(str.split, fin)
    ]

seen_indices = set()
generator = 0
index = 0

while index not in seen_indices:
    seen_indices.add(index)
    isntr, value = instructions[index]
    if isntr == "acc":
        generator += value
        index += 1

    elif isntr == "jmp":
        index += value
        continue
    elif isntr == "nop":
        index += 1
print(f"Part 1: {generator}")

with open("input.txt") as fin:
    instructions = []
    corrupt = []
    for operation, argument in map(str.split, fin):
        if operation != "acc":
            corrupt.append(len(instructions))
        instructions.append((operation, int(argument)))

corrupt_map = {"jmp": "nop", "nop": "jmp"}

for possibly_corrupted in corrupt:
    isntr_corr, value_corr = instructions[possibly_corrupted]
    A = isntr_corr
    if isntr_corr == "jmp":
        isntr_corr = "nop"
    elif isntr_corr == "nop":
        isntr_corr = "jmp"
    instructions[possibly_corrupted] = isntr_corr, value_corr
    seen_indices = set()
    generator = 0
    index = 0
    while index not in seen_indices and index < len(instructions):
        seen_indices.add(index)
        operation, argument = instructions[index]
        if operation == "acc":
            generator += argument
        elif operation == "jmp":
            index += argument
            continue
        index += 1
    if index == len(instructions):
        break
    instructions[possibly_corrupted] = A, value_corr

print(f"Part 2: {generator}")
