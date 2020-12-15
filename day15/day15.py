import os

start_values = [8, 13, 1, 0, 18, 9]

seen = {8: 1, 13: 2, 1: 3, 0: 4, 18: 5, 9: 6}

def next_value(values, seen):
    element = values[-1]
    if values.count(element) == 1:
        values.append(0)
        seen[element] = len(values) - 1
    else:
        value_1 = values[-1]
        b = len(values)
        values.append(b - seen[element])
        seen[value_1] = b
    return values


while True:
    start_values = next_value(start_values, seen)
    if len(start_values) == 2020:
        break

#print(f'Part : {start_values[2020 - 1]}')
#print(f'Part : {start_values[30000000 - 1]}')
