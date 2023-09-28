def part_1(inputs: list):
    cycle_number = 1
    registry_value = 1
    cycle_values = {cycle_number: registry_value}
    for x in inputs:
        if x[0].strip() == "addx":
            cycle_number += 1
            cycle_values[cycle_number] = registry_value
            cycle_number += 1
            registry_value += x[1]
        else:
            cycle_number += 1
        cycle_values[cycle_number] = registry_value
    return cycle_values


def part_two(inputs) -> None:
    drawn = []
    for position in range(240):
        cycle = position + 1
        register_val = inputs[cycle]
        if -1 <= position % 40 - register_val <= 1:
            drawn.append(position)
    for k in range(6):
        for i in range(40):
            if i + k * 40 in drawn:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    with open("input.txt") as fin:
        lines = [fin.strip() for fin in fin.readlines()]
    inputs = []
    for line in lines:
        splitted = line.split(" ")
        if len(splitted) == 2:
            inputs.append([splitted[0], int(splitted[1])])
        else:
            inputs.append(splitted)
    to_check = [20, 60, 100, 140, 180, 220]
    parsed = part_1(inputs)

    print(f"response part 1 {sum(x * v for x, v in parsed.items() if x in to_check)}")
    part_two(parsed)
