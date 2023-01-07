import copy

with open("input.txt") as fin:
    grid = [list(jolt.strip()) for jolt in fin]


def pprint(a):
    print("------------------")
    for rows in a:
        print(rows, sep="\n")


def occupied_adjacent(a, x, y):
    places = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    ]
    return sum(
        1
        for place in places
        if 0 <= place[0] <= (len(a) - 1)
        and 0 <= place[1] <= (len(a[0]) - 1)
        and a[place[0]][place[1]] == "#"
    )


def rules(_grid, x, y):
    status = _grid[x][y]
    if status == "L" and occupied_adjacent(_grid, x, y) == 0:
        return "#"
    elif status == "#" and occupied_adjacent(_grid, x, y) >= 4:
        return "L"
    return status


different = True
passages = 0
while True:
    passages += 1
    newgrid = []
    for row in range(0, len(grid)):
        newline = []
        for columns in range(0, len(grid[0])):
            newline.append(rules(grid, row, columns))
        newgrid.append(newline)
    if grid == newgrid:
        break
    else:
        grid = copy.deepcopy(newgrid)

occupied_places = 0

for row in range(len(grid)):
    for column in range(len(grid[0])):
        occupied_places += grid[row][column] == "#"

print(f"Part 1: {occupied_places}")


def rules_part_2(_grid, x, y):
    status = _grid[x][y]
    if status == "L" and occupied_non_adjacent(_grid, x, y) == 0:
        return "#"
    elif status == "#" and occupied_non_adjacent(_grid, x, y) >= 5:
        return "L"
    return status


def occupied_non_adjacent(a, x, y):
    occupied_seats = 0
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for place in vectors:
        index = 1
        found = False
        while not found:
            _ = tuple(index * x for x in place)
            sum_values = (x + _[0], y + _[1])
            if 0 <= sum_values[0] <= (len(a) - 1) and 0 <= sum_values[1] <= (
                len(a[0]) - 1
            ):
                if a[sum_values[0]][sum_values[1]] == "#":
                    occupied_seats += 1
                    found = True
                elif a[sum_values[0]][sum_values[1]] == "L":
                    found = True
                index += 1
            else:
                break
    return occupied_seats


with open("input.txt") as fin:
    grid = [list(jolt.strip()) for jolt in fin]

different = True
passages = 0
while True:
    passages += 1
    newgrid = []
    for row in range(0, len(grid)):
        newline = []
        for columns in range(0, len(grid[0])):
            newline.append(rules_part_2(grid, row, columns))
        newgrid.append(newline)
    if grid == newgrid:
        break
    else:
        grid = copy.deepcopy(newgrid)

occupied_places = 0
for row in range(len(grid)):
    for column in range(len(grid[0])):
        occupied_places += grid[row][column] == "#"

print(f"Part 2: {occupied_places}")
