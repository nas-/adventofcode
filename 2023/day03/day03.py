from pathlib import Path


def check_neightbours(grid, x, y):
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
    for place in places:
        if not is_valid(place[0], place[1], grid):
            continue
        el = grid[place[0]][place[1]]
        if el != "." and not el.isdigit():
            return x, y
    return None


def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def solve_part_1(puzzle_input):
    solution_part_1 = 0
    for row in range(len(puzzle_input)):
        number = ""
        valid = False
        for col in range(len(puzzle_input[0])):
            el = puzzle_input[row][col]
            if el.isdigit():
                number += puzzle_input[row][col]
                valid_position = check_neightbours(puzzle_input, row, col)
                if valid_position:
                    valid = True
            else:
                if number and valid:
                    solution_part_1 += int(number.strip())
                number = ""
                valid = False
        if number and valid:
            solution_part_1 += int(number.strip())
    return solution_part_1


if __name__ == "__main__":
    puzzle_input = (Path(__file__).parent / "input").read_text().splitlines()
    puzzle_input = [list(x) for x in puzzle_input]
    part_1 = solve_part_1(puzzle_input)
    print(f"solution part 1 {part_1}")
