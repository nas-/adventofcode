import copy
import functools
import itertools
import os
import re

fin = open("input.txt", "r")

data = [data for data in fin.read().split("\n\n")]
a, my, c = data
my = list(map(int, my.split("\n")[-1].strip().split(",")))
rules = {}
for a in a.split("\n"):
    x = a.split(":")[0].strip()
    min1, max1, min2, max2 = map(int, re.findall(r"\d{1,3}", a))
    rules[x] = set(range(min1, max1 + 1)).union(set(range(min2, max2 + 1)))

nearby = [list(map(int, a.split(","))) for a in c.split("\n")[1:]]

counters = 0
for c in nearby:
    valid = all(any(element in k for k in rules.values()) for element in c)
    if not valid:
        for element in c:
            if all(element not in a for a in rules.values()):
                counters += element

print(f"Part 1: {counters}")

nearby_valid = []
for c in nearby:
    valid = all(any(element in k for k in rules.values()) for element in c)
    if valid:
        nearby_valid.append(c)

transpose_matrix = [list(row) for row in zip(*nearby_valid)]
matrix = {}
for x in rules:
    w = [all(y in rules[x] for y in i) for i in transpose_matrix]
    matrix[x] = {"order": sum(w), "columns": w}
matrix1 = {k: v for k, v in sorted(matrix.items(), key=lambda item: item[1]["order"])}

my_fields = {}
for element, value in matrix1.items():
    for i, a in enumerate(value["columns"]):
        if a and i not in my_fields.values():
            my_fields[element] = i
            break
mult = 1
for x in my_fields:
    if x.startswith("departure"):
        mult *= my[my_fields[x]]
print(f"Part 2: {mult}")
