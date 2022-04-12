from collections import Counter
from functools import lru_cache


def get_inputs(file):
    with open(file) as file:
        numbers = map(int, file.readlines()[0].strip().split(','))
        return Counter(numbers)


def process_positions(positions, position_to_move):
    fuel = 0
    for k, v in positions.items():
        fuel += v * abs(k - position_to_move)
    return fuel


def optimize(range_to_search, pos, fun):
    d = {'fuel': 1e500, 'position': -1}
    for i in range_to_search:
        fuel = fun(pos, i)
        if fuel < d['fuel']:
            d['fuel'] = fuel
            d['position'] = i
    return d


def process_positions_part_2(positions, position_to_move):
    fuel = 0
    for k, v in positions.items():
        fuel += calculate_fuel(k, v, position_to_move)
    return fuel


@lru_cache(10000)
def calculate_fuel(k, v, position_to_move):
    n = abs(k - position_to_move)
    return v * n * (n + 1) / 2


positions = get_inputs('input')
min_value = min(positions.keys())
max_value = max(positions.keys())

print(f'Part 1: {optimize(range(min_value, max_value + 1), positions, process_positions)}')
print(f'Part 2: {optimize(range(min_value, max_value + 1), positions, process_positions_part_2)}')
