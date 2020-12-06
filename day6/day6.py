fin = open("input.txt", "r")

data = [data for data in fin.read().split("\n\n")]
part1 = sum(len(set(x.replace('\n', '').strip())) for x in data)
print(f'Part 1: {part1}')

total = 0
for x in data:
    y = x.replace(' ', '').strip().split('\n')
    k = []
    for z in y:
        k.append(set(z))
    total += len(set.intersection(*k))

print(f'Part 2: {total}')
