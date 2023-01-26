from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Move:
    amount: int
    from_stack: int
    to_stack: int

    @classmethod
    def from_line(cls, line: str):
        splitted = line.split(" ")
        revalue = cls(amount=int(splitted[1]), from_stack=int(splitted[3]), to_stack=int(splitted[-1]))
        return revalue


def first_part(ship_state, moves):
    ship = deepcopy(ship_state)
    for move in moves:
        to_move = list(reversed(ship[move.from_stack][-move.amount:]))
        remaining = ship[move.from_stack][:-move.amount]
        ship[move.from_stack] = remaining
        ship[move.to_stack].extend(to_move)

    return "".join([ship[k][-1] for k in ship])


def second_part(ship_state, moves):
    ship = deepcopy(ship_state)
    for move in moves:
        to_move = list(ship[move.from_stack][-move.amount:])
        remaining = ship[move.from_stack][:-move.amount]
        ship[move.from_stack] = remaining
        ship[move.to_stack].extend(to_move)

    return "".join([ship[k][-1] for k in ship])


if __name__ == '__main__':
    with open("input.txt") as fin:
        inputs = fin.read()
    initial_config, commands = inputs.split("\n\n")
    command_list = []
    for command in commands.split("\n"):
        command_list.append(Move.from_line(command))
    docker = {}
    last_line = initial_config.split("\n")[-1]
    indexes = {}
    for char in last_line:
        if char != " ":
            indexes[int(char)] = last_line.index(char)


    for line in reversed(initial_config.split("\n")[:-1]):
        for key, value in indexes.items():
            try:
                val = line[value]
            except IndexError:
                continue
            if val != " ":
                docker[key] = docker.get(key, [])
                docker[key].append(val)
    print(indexes)
    print(docker)

    print(f"First part result is {first_part(docker, command_list)}, expected test-> CMZ actual-> RFFFWBPNS")
    print(f"Second part result is {second_part(docker, command_list)}, expected test-> MCD actual-> CQQBBJFCS")
