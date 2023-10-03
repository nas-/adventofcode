from datetime import datetime


def parse_input(fin):
    parsed = fin.read().rstrip().replace("\n\n", "\n").split("\n")
    return parsed


def comparison(a, b):
    a_is_int = isinstance(a, int)
    b_is_int = isinstance(b, int)

    if a_is_int and b_is_int:
        return a - b
    if a_is_int != b_is_int:
        if a_is_int:
            return comparison([a], b)
        else:
            return comparison(a, [b])

    for i, j in zip(a, b):
        res = comparison(i, j)
        if res != 0:
            return res
    return len(a) - len(b)


def custom_sort(paired) -> list:
    result = []
    for i, (a, b) in enumerate(paired):
        is_sorted = comparison(a, b)
        if is_sorted < 0:
            result.append(i + 1)
    return result


def sorting(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - j - 1):
            res = comparison(arr[i], arr[i + 1])
            if res > 0:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return arr


if __name__ == "__main__":
    time = datetime.now()
    grid = parse_input(open("input.txt"))
    parsed = [(eval(grid[i]), eval(grid[i + 1])) for i in range(0, len(grid), 2)]
    res = custom_sort(parsed)
    print(f"Part 1: {sum(res)}")
    divpackets = [[[2]], [[6]]]

    grid.extend(("[[2]]", "[[6]]"))
    parsed = sorting([eval(x) for x in grid])

    x, y = parsed.index(divpackets[0]) + 1, parsed.index(divpackets[1]) + 1
    print(
        f"Part 2: {x * y}, elapsed time: {(datetime.now() - time).total_seconds()* 1000}ms"
    )
