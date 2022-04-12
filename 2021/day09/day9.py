def get_inputs(file):
    with open(file) as file:
        lines = file.readlines()
        inputs = [list(map(int, list(x.strip()))) for x in lines]
    return inputs


def calculate_low_points(data):
    low_points = []
    for x, val in enumerate(data):
        for y, num in enumerate(val):
            cond = []
            cond.append(compute_adjacent(data, x + 1, y, data[x][y]))
            cond.append(compute_adjacent(data, x - 1, y, data[x][y]))
            cond.append(compute_adjacent(data, x, y + 1, data[x][y]))
            cond.append(compute_adjacent(data, x, y - 1, data[x][y]))
            if all(cond):
                low_points.append((x, y))
            cond = []
    return low_points


def compute_adjacent(data, x, y, num):
    if x < 0 or y < 0:
        return True
    try:
        return data[x][y] > num
    except IndexError:
        return True


def neighbours(y, x):
    neighs = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return [(a, b) for a, b in neighs if 0 <= a < N and 0 <= b < M]


def calculate_basin(x, y):
    basin = {(x, y)}
    for a, b in neighbours(x, y):
        if height_map[x][y] < height_map[a][b] < 9:
            basin=basin.union(calculate_basin(a, b))
    return basin


height_map = get_inputs('input')
N = len(height_map)
M = len(height_map[0])
low_points = calculate_low_points(height_map)
print(f'Part 1: {sum((1 + height_map[x][y]) for x, y in low_points)}')
basins = sorted([calculate_basin(x, y) for x, y in low_points],key=lambda x:len(x))
print(f'Part 2: {len(basins[-1])*len(basins[-2])*len(basins[-3])}')

pass
