def ref():
    with open('input') as file:
        text = map(str.strip, file.readlines())
    return [[a.split(' ')[0], int(a.split(' ')[1])] for a in text]


def part_1(data):
    coords = {"x": 0, "y": 0}
    for a in data:
        if a[0] == 'forward':
            coords['x'] += a[1]
        elif a[0] == 'down':
            coords['y'] += a[1]
        elif a[0] == 'up':
            coords['y'] -= a[1]
    return coords['x'] * coords['y']


def part_2(data):
    coords = {"x": 0, "y": 0, "aim": 0}
    for a in data:
        if a[0] == 'down':
            coords['aim'] += a[1]
        elif a[0] == 'up':
            coords['aim'] -= a[1]
        elif a[0] == 'forward':
            coords['x'] += a[1]
            coords['y'] += a[1] * coords['aim']
    return coords['x'] * coords['y']


if __name__ == '__main__':
    data = ref()
    print(part_1(data))
    print(part_2(data))
