def parse_input(data):
    lines = [line.strip().split() for line in data.splitlines()]
    grid = [list(line[0]) for line in lines]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = int(grid[i][j])
    return grid


def is_visible(grid, i, j):
    element = grid[i][j]
    visibility_dict = {"left": False, "right": False, "top": False, "down": False}
    is_edge = False
    if i == 0:
        visibility_dict["top"] = True
        is_edge = True
    if i == len(grid) - 1:
        visibility_dict["down"] = True
        is_edge = True
    if j == 0:
        visibility_dict["left"] = True
        is_edge = True
    if j == len(grid[i]) - 1:
        visibility_dict["right"] = True
        is_edge = True
    if is_edge is False:
        # check left
        visibility_left = all(
            element > x for x in [grid[i][k] for k in range(j - 1, -1, -1)]
        )
        visibility_dict["left"] = visibility_left
        # check right
        visibility_right = all(
            element > x for x in [grid[i][w + 1] for w in range(j, len(grid[i]) - 1)]
        )
        visibility_dict["right"] = visibility_right
        #  check top
        visibility_top = all(
            element > x for x in [grid[k][j] for k in range(i - 1, -1, -1)]
        )
        visibility_dict["top"] = visibility_top
        # check down
        visibility_down = all(
            element > x for x in [grid[w + 1][j] for w in range(i, len(grid) - 1)]
        )
        visibility_dict["down"] = visibility_down
    return any(visibility_dict.values())


def can_see_trees_in_direction(row, col, dr, dc):
    height = grid[row][col]
    distance = 0

    while True:
        row += dr
        col += dc

        if (0 <= row < len(grid) and 0 <= col < len(grid[row])) is False:
            return distance

        if grid[row][col] < height:
            distance += 1
        else:
            return distance + 1


def scenic_score(row, col):
    up = can_see_trees_in_direction(row, col, -1, 0)
    left = can_see_trees_in_direction(row, col, 0, -1)
    right = can_see_trees_in_direction(row, col, 0, 1)
    down = can_see_trees_in_direction(row, col, 1, 0)

    return up * down * left * right


def highest_scenic_score(grid):
    max_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            score = scenic_score(row, col)
            max_score = max(max_score, score)

    return max_score


if __name__ == "__main__":
    with open("input.txt") as fin:
        grid = parse_input(fin.read().strip())
    new_grid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = is_visible(grid, i, j)
    total_visible = sum([sum(row) for row in new_grid])
    print(total_visible)

    max_value = highest_scenic_score(grid)
    print(max_value)
