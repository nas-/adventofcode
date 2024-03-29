def parse_input(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        return [
            (d, int(v))
            for (d, v) in [tuple(line.strip().split()) for line in f.readlines()]
        ]


def part_one(moves) -> int:
    tail = head = (0, 0)
    tail_visited = {tail}
    for d, v in moves:
        for _ in range(v):
            dx, dy = move_knot(d)
            head = (head[0] + dx, head[1] + dy)
            tail = adjust_tail(tail, head)
            tail_visited.add(tail)
    return len(tail_visited)


def part_two(moves) -> int:
    knots = [(0, 0) for _ in range(10)]
    tail_visited = {knots[-1]}
    for d, v in moves:
        for _ in range(v):
            dx, dy = move_knot(d)
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(1, len(knots)):
                knots[i] = adjust_tail(knots[i], knots[i - 1])
            tail_visited.add(knots[-1])
    return len(tail_visited)


def move_knot(direction: str):
    dir_to_move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }
    return dir_to_move[direction]


def adjust_tail(tail, head):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail[0], tail[1]
    elif dx == 0:
        return tail[0], tail[1] + dy // abs(dy)
    elif dy == 0:
        return tail[0] + dx // abs(dx), tail[1]
    else:
        return tail[0] + dx // abs(dx), tail[1] + dy // abs(dy)


if __name__ == "__main__":
    inputs = parse_input("input.txt")
    print(f"Result for part 1: {part_one(inputs)}")
    print(f"Result for part 2: {part_two(inputs)}")
