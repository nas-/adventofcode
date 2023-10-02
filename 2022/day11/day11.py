import operator
from functools import reduce


class Monkey:
    def __init__(
        self,
        id: int,
        starting_items: list[int],
        operation: str,
        divisible_by: int,
        value_true,
        value_false,
    ):
        self.id = id
        self.starting_items = starting_items

        if "old * old" == operation:
            self.operator = operator.pow
            self.operand = 2
        elif "old + old" in operation:
            self.operator = operator.mul
            self.operand = 2
        elif "old +" in operation:
            self.operator = operator.add
            self.operand = int(operation.split(" ")[-1])
        elif "old *" in operation:
            self.operator = operator.mul
            self.operand = int(operation.split(" ")[-1])

        self.divisible_by = divisible_by
        self.value_true = value_true
        self.value_false = value_false
        self.count_inspections = 0

    def __str__(self):
        return f"Monkey {self.id}: {self.starting_items}, {self.operator}, {self.operand}, {self.divisible_by}, {self.value_true}, {self.value_false}"


def parse_input(data):
    blocks = [line.strip().split("\n") for line in data.split("\n\n")]
    monkey_list = {}
    for block in blocks:
        a = Monkey(
            id=int(block[0].split(" ")[1].strip(":")),
            starting_items=[
                int(item.strip()) for item in block[1].split(":")[1].split(",")
            ],
            operation=" ".join(block[2].split(" ")[-3:]),
            divisible_by=int(block[3].split(" ")[-1]),
            value_true=int(block[4].split(" ")[-1]),
            value_false=int(block[5].split(" ")[-1]),
        )
        monkey_list[a.id] = a

    return monkey_list


def play_round(monkeylist, worry_level):
    my_worry_level = reduce(
        operator.mul, [monkey.divisible_by for monkey in monkeylist.values()], 1
    )
    for monkey_id in monkeylist.keys():
        monkey = monkeylist[monkey_id]
        if len(monkey.starting_items) == 0:
            continue
        monkey.count_inspections += len(monkey.starting_items)
        for item in monkey.starting_items:
            new = monkey.operator(item, monkey.operand) // worry_level % my_worry_level
            if new % monkey.divisible_by == 0:
                monkeylist[monkey.value_true].starting_items.append(new)
            else:
                monkeylist[monkey.value_false].starting_items.append(new)
        monkey.starting_items = []


def play(worry_level, rounds=20):
    with open("input.txt") as fin:
        monkeylist = parse_input(fin.read().strip())
    for _ in range(rounds):
        play_round(monkeylist, worry_level)
    inspections = sorted([monkey.count_inspections for monkey in monkeylist.values()])
    return inspections[-1] * inspections[-2]


if __name__ == "__main__":
    part_1_answer = play(worry_level=3, rounds=20)
    print(f"Part 1: {part_1_answer}")
    part_2_answer = play(worry_level=1, rounds=10000)
    print(f"Part2: {part_2_answer}")
