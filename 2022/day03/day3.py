import itertools

def score(caracter_ord):
    if caracter_ord < 91:
        # Uppercase
        return caracter_ord - 65 + 27
    return caracter_ord - 97 + 1


with open("input.txt") as fin:
    inputs = [jolt.strip() for jolt in fin]




def first_part(inputs):
    total = 0
    for input in inputs:
        midpoint = (len(input) // 2)
        first, second = input[:midpoint], input[midpoint:]
        common = set(first).intersection(second)
        total += score(ord(common.pop()))
    return total


def second_part(inputs):
    new_grouped = []
    for i in range(len(inputs) // 3):
        new_grouped.append(inputs[i * 3:(i + 1) * 3])
    total = 0
    for group in new_grouped:
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total += score(ord(common.pop()))
    return total


print(f"First part result is {first_part(inputs)}, expected 8139")
print(f"Second part result is {second_part(inputs)}, expected 2668")

