with open('input') as file:
    text = [a.strip() for a in file.readlines()]


def part_1(text):
    result = []
    result2 = []
    for k in range(len(text[0])):
        acc = 0
        for i in text:
            acc += int(i[k])
        if acc > (len(text) + 1) / 2:
            result.append('1')
            result2.append('0')
        else:
            result.append('0')
            result2.append('1')
    return int(''.join(result), 2) * int(''.join(result2), 2)


def part_2(text):
    return part_2_1(text, False) * part_2_1(text, True)


def part_2_1(text, part_1):
    for k in range(len(text[0])):
        acc = 0
        for i in text:
            acc += int(i[k])
        if acc >= (len(text)) / 2:
            caracter = '1'

        else:
            caracter = '0'
        w = []
        for i in text:
            if part_1:
                if i[k] != caracter:
                    w.append(i)
            else:
                if i[k] == caracter:
                    w.append(i)
        text = w
        if len(text) == 1:
            return int(text[0], 2)


print(part_1(text))
print(part_2(text))
