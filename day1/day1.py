fin = open("input.txt", "r")

data = [int(data) for data in fin.readlines()]
part1, part2 = False, False
for x in data:
    for y in data:
        if x + y == 2020 and not part1:
            print(f'Part 1:{x * y}')
            part1 = True
        for z in data:
            if x + y + z == 2020 and not part2:
                part2 = True
                print(f'Part 2: {x * y * z}')
