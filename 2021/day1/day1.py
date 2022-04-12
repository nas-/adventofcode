def part_1(x):
    increase = 0
    for i, a in enumerate(x):
        if i == 0:
            continue
        if a > x[i - 1]:
            increase += 1
    return increase


with open('input') as file:
    text = list(map(int, map(str.strip, file.readlines())))

print(f'part 1 {part_1(text)}')
print(f'part 2 {part_1([sum(text[b] for b in range(i - 2, i + 1)) for i, a in enumerate(text) if i > 1])}')
