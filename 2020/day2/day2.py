fin = open("input.txt", "r")

data = [data for data in fin.readlines()]

part1 = 0
part2 = 0
for item in data:
    B = item.split(' ')
    low_bound, high_bound = map(int, B[0].split('-'))
    char = B[1][0]
    count = list(B[-1]).count(char)
    part1 += low_bound <= count <= high_bound
    if bool(B[-1][low_bound - 1] == char) ^ bool(B[-1][high_bound - 1] == char):
        part2 += 1
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
