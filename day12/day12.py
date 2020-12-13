import os
from functools import reduce
import copy
import math

with open("input.txt") as fin:
    inputs = [jolt.strip() for jolt in fin]


def handle_position(single_order, pos):
    let = single_order[0]
    am = int(single_order[1:])
    if let == 'N':
        return [pos[0] + am, pos[1], pos[2]]
    elif let == 'S':
        return [pos[0] - am, pos[1], pos[2]]
    elif let == 'E':
        return [pos[0], pos[1] + am, pos[2]]
    elif let == 'W':
        return [pos[0], pos[1] - am, pos[2]]
    elif let == 'L':
        return [pos[0], pos[1], pos[2] - am]
    elif let == 'R':
        return [pos[0], pos[1], pos[2] + am]
    elif let == 'F':
        heading = pos[2]
        E = am * math.sin(math.radians(heading))
        N = am * math.cos(math.radians(heading))
        return [pos[0] + N, pos[1] + E, pos[2]]


position = [0, 0, 90]
for order in inputs:
    position = handle_position(order, position)

print(f'Part 1: {int(round(abs(position[0]) + abs(position[1])))}')

rotations = {
    "R90": [[0, 1], [-1, 0]], "R180": [[-1, 0], [0, -1]], "R270": [[0, -1], [1, 0]],
    "L90": [[0, -1], [1, 0]], "L180": [[-1, 0], [0, -1]], "L270": [[0, 1], [-1, 0]]
}


def rotate(position2, deg):
    r = rotations[deg]
    _x, _y = position2
    return [_x * r[1][1] + _y * r[1][0], _x * r[0][1] + _y * r[0][0]]


x = y = 0
waypoint = [1, 10]

for order in inputs:
    letter = order[0]
    amount = int(order[1:])
    if letter == 'N':
        waypoint[0] += amount
    elif letter == 'S':
        waypoint[0] -= amount
    elif letter == 'E':
        waypoint[1] += amount
    elif letter == 'W':
        waypoint[1] -= amount
    elif letter in ['L', 'R']:
        waypoint = rotate(waypoint, order)
    elif letter == 'F':
        x += waypoint[1] * amount
        y += waypoint[0] * amount

print(f'Part 2: {abs(x) + abs(y)}')
