start_values = [8, 13, 1, 0, 18, 9]


# seen = {8: 1, 13: 2, 1: 3, 0: 4, 18: 5, 9: 6}


def next_value(last, index, seen):
    seen[last] = index
    return index - seen.get(last, index)


steps, ns = 30000000, [8, 13, 1, 0, 18, 9]
last = ns[-1]
seen = {n: i for i, n in enumerate(ns)}
for i in range(len(ns) - 1, steps - 1):
    seen[last], last = i, i - seen.get(last, i)
print(last)
