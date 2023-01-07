fin = open("input.txt")

data = [data.strip() for data in fin.readlines()]


def slope(y, x):
    tree = 0
    for i, el in enumerate(data):
        if i % y == 0:
            element = (int((i * x) / y)) % len(el)
            if el[element] == "#":
                tree += 1
    return tree


print(f"Part 1: {slope(1, 3)}")
print(f"Part 2: {slope(1, 1) * slope(1, 3) * slope(1, 5) * slope(1, 7) * slope(2, 1)}")
