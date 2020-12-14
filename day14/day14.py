import os
import functools
import copy
import itertools

fin = open("input.txt", "r")

mems = []
for b, data in enumerate(fin.readlines()):
    if data.startswith('mem'):
        mems.append((b, int(data.split('[')[1].split(']')[0], 0), int(data.split('=')[1].strip())))
    elif data.startswith('mask'):
        mems.append((b, data.split('=')[-1].strip()))


def binario(numero, msk):
    bin_number = str(bin(numero))[2:].zfill(36)
    nuovo_numero = []
    for i, c in enumerate(msk):
        if c == 'X':
            nuovo_numero.append(bin_number[i])
        elif c == '1':
            nuovo_numero.append('1')
        elif c == '0':
            nuovo_numero.append('0')
    return int(''.join(nuovo_numero), 2)


a = {}

mask = ''
for instruction in mems:
    if len(instruction) == 2:
        mask = instruction[1]
        continue
    else:
        a[instruction[1]] = binario(instruction[2], mask)
print(f'Part 1: {sum(a.values())}')


def binario_pt_2(numero, msk):
    bin_number = str(bin(numero))[2:].zfill(36)
    nuovo_numero = []
    for i, c in enumerate(msk):
        if c == '0':
            nuovo_numero.append(bin_number[i])
        elif c == '1':
            nuovo_numero.append('1')
        elif c == 'X':
            nuovo_numero.append('X')
    Xes = nuovo_numero.count('X')
    total_elements = []
    for k in itertools.product('01', repeat=Xes):
        newelement = []
        index = 0
        for _ in nuovo_numero:
            if _ == 'X':
                newelement.append(k[index])
                index += 1
            else:
                newelement.append(_)
        total_elements.append(''.join(newelement))
    return [int(x, 2) for x in total_elements]


a = {}

mask = ''
for instruction in mems:
    if len(instruction) == 2:
        mask = instruction[1]
        continue
    else:
        for element in binario_pt_2(instruction[1], mask):
            a[element] = instruction[2]

print(f'Part 2: {sum(a.values())}')
