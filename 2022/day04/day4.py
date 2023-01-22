def first_part(rows: list[list[str]]) -> int:
    counter = 0
    for rows in rows:
        first_set, second_set = generate_sets(rows)
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            counter += 1
    return counter


def generate_sets(row: list[str]) -> tuple[set, set]:
    first_area = [int(x) for x in row[0].split("-")]
    second_area = [int(x) for x in row[1].split("-")]
    first_set = set(x for x in range(first_area[0], first_area[1] + 1))
    second_set = set(x for x in range(second_area[0], second_area[1] + 1))
    return first_set, second_set


#
def second_part(rows: list[list[str]]) -> int:
    counter = 0
    for rows in rows:
        first_set, second_set = generate_sets(rows)
        if first_set.intersection(second_set) != set():
            counter += 1
    return counter


if __name__ == '__main__':
    with open("input.txt") as fin:
        inputs: list[list[str]] = [jolt.strip().split(",") for jolt in fin]
    print(f"First part result is {first_part(inputs)}, expected 466")
    print(f"Second part result is {second_part(inputs)}, expected 2668")
