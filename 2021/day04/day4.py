def get_imputs_boards(file):
    with open(file) as file:
        lines = [a.strip() for a in file.readlines()]
        numbers = map(int, lines[0].split(","))
        boards = []
        board = []
        for line in lines[2:]:
            if not line:
                boards.append(board)
                board = []
            elif line == lines[-1]:
                board.append(list(map(int, [a for a in line.split(" ") if a])))
                boards.append(board)
                board = []
            else:
                board.append(list(map(int, [a for a in line.split(" ") if a])))
    return numbers, boards


def process_board(number, board):
    for x in board:
        for i, y in enumerate(x):
            if y == number:
                x[i] = -1
    for x in board:
        if all(y == -1 for y in x):
            return get_score(number, board)
    for n in range(len(board[0])):
        if all(x == -1 for x in [x[n] for x in board]):
            return get_score(number, board)


def get_score(number, board):
    return number * sum(sum(x for x in i if x > 0) for i in board)


def process_multiple(numbers, boards):
    for number in numbers:
        for board in boards:
            test = process_board(number, board)
            if test:
                return test


def part_2(numbers, boards):
    show_score = False
    boards_to_play = boards
    for number in numbers:
        boards_to_iter = boards_to_play
        boards_to_play = []
        if len(boards_to_iter) == 1:
            show_score = True
        for board in boards_to_iter:
            test = process_board(number, board)
            if not test:
                boards_to_play.append(board)
        if show_score:
            if test:
                return test


numbers, boards = get_imputs_boards("input")
print(process_multiple(numbers, boards))
print(part_2(numbers, boards))
