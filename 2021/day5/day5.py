from collections import Counter


def get_inputs(file):
    with open(file) as file:
        lines = [a.strip() for a in file.readlines()]
    coords = []
    for i, line in enumerate(lines):
        start, end = line.split('->')
        start = list(map(int, start.strip().split(',')))
        end = list(map(int, end.strip().split(',')))
        # if start[0] == end[0] or start[1] == end[1]:
        coords.append({'x1': start[0], 'y1': start[1], 'x2': end[0], 'y2': end[1]})

    return coords


def process_part_1(x):
    points = []
    x = [y for y in x if y['x1'] == y['x2'] or y['y1'] == y['y2']]
    for a in x:
        if a['x1'] == a['x2']:
            y_range = list(range(min(a['y1'], a['y2']), max(a['y1'], a['y2']) + 1))
            for y in y_range:
                points.append((a['x1'], y))
        elif a['y1'] == a['y2']:
            x_range = range(min(a['x1'], a['x2']), max(a['x1'], a['x2']) + 1)
            for y in x_range:
                points.append((y, a['y1']))
        else:
            print('xx')
    return sum(1 for y in Counter(points).values() if y >= 2)


def part_2(x):
    points = []
    for a in x:
        if a['x1'] == a['x2']:
            y_range = list(range(min(a['y1'], a['y2']), max(a['y1'], a['y2']) + 1))
            for y in y_range:
                points.append((a['x1'], y))
        elif a['y1'] == a['y2']:
            x_range = range(min(a['x1'], a['x2']), max(a['x1'], a['x2']) + 1)
            for y in x_range:
                points.append((y, a['y1']))
        else:
            # diagonal
            x_gap = a['x1'] - a['x2']
            x_dir = -1 if x_gap > 0 else 1
            y_gap = a['y1'] - a['y2']
            y_dir = -1 if y_gap > 0 else 1
            rangex = list(range(a['x1'], a['x1'] - x_gap + x_dir, x_dir))
            rangey = list(range(a['y1'], a['y1'] - y_gap + y_dir, y_dir))
            points.extend(zip(rangex, rangey))

    return sum(1 for y in Counter(points).values() if y >= 2)


inputs = part_2(get_inputs('input'))
print(f'{inputs}')
