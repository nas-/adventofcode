from collections import deque
from datetime import datetime
from functools import lru_cache


def parse_input(data):
    lines = [line.strip().split() for line in data.splitlines()]
    grid = [list(line[0]) for line in lines]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = grid[i][j]
    return grid


@lru_cache(maxsize=None)
def get_current_height(char: str):
    if char == "S":
        return ord("a")
    elif char == "E":
        return ord("z")
    else:
        return ord(char)


@lru_cache(maxsize=None)
def get_neighbors(x, y):
    current_height = get_current_height(grid[x][y])
    h, w = len(grid), len(grid[0])
    possible_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    postions = []
    for pos in possible_positions:
        if 0 <= pos[0] < h and 0 <= pos[1] < w:
            position_height = get_current_height(grid[pos[0]][pos[1]])
            if position_height <= current_height + 1:
                postions.append(pos)
    return postions


def step(source, destination):
    queue = deque([(0, source)])
    visited = set()
    while queue:
        distance, rc = queue.popleft()
        if rc == destination:
            return distance
        if rc not in visited:
            visited.add(rc)
            neighbors = get_neighbors(rc[0], rc[1])
            for n in neighbors:
                if n not in visited:
                    queue.append((distance + 1, n))

    return float("inf")


def part_1(grid: list[list[str]]):
    starting_pos = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == "S"
    ][0]
    end_pos = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == "E"
    ][0]
    steps = step(starting_pos, end_pos)
    return steps


def part_2(grid: list[list[str]]):
    starting_pos = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] in ["a", "S"]
    ]
    end_pos = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == "E"
    ][0]
    min_steps = float("inf")
    for pos in starting_pos:
        steps = step(pos, end_pos)
        if steps < min_steps:
            min_steps = steps
    return min_steps


if __name__ == "__main__":
    with open("input.txt") as fin:
        grid = parse_input(fin.read().strip())
    start_time = datetime.now()
    part_1_ans = part_1(grid)
    print(
        f"Part One: {part_1_ans}, elapsed time: {(datetime.now() - start_time).total_seconds()*1000} ms"
    )
    start_time2 = datetime.now()
    part_2_ans = part_2(grid)
    print(
        f"Part Two: {part_2_ans}, elapsed time: {(datetime.now() - start_time2).total_seconds()*1000} ms"
    )
