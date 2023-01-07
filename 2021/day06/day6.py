from collections import Counter, defaultdict


def get_inputs(file):
    with open(file) as file:
        numbers = map(int, file.readlines()[0].strip().split(","))
        return list(numbers)


fishes = get_inputs("input")


def process_day(fish_school, days=1):
    a = defaultdict(int)
    a.update(Counter(fish_school))
    for day in range(days):
        a = {x - 1: y for x, y in a.items()}
        b = a.copy()
        for k, v in a.items():
            if k < 0:
                b.pop(k)
                b.update({6: a.get(6, 0) + v})
                b.update({8: a.get(8, 0) + v})
        a = b
    return sum(a.values())


print(f"Part 1: {process_day(fishes, 80)}")
print(f"Part 2: {process_day(fishes, 256)}")
