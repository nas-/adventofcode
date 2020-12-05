fin = open("input.txt", "r")

TICKETS = [data.strip() for data in fin.readlines()]


def front(a, b):
    el = b - a
    return a, int(b - el / 2)


def back(a, b):
    el = b - a + 1
    return int(a + el / 2), b


def place(low_bound, up_bound, element):
    for row in element:
        if up_bound - low_bound == 1:
            if row in ['F', 'L']:
                return low_bound
            else:
                return up_bound
        if row in ['F', 'L']:
            low_bound, up_bound = front(low_bound, up_bound)
        else:
            low_bound, up_bound = back(low_bound, up_bound)
    return low_bound, up_bound


def calculate_index(ticket):
    row = place(0, 127, ticket[:-3])
    seat = place(0, 7, ticket[-3:])
    return row * 8 + seat


tickketsid = sorted([calculate_index(data) for data in TICKETS])

for ticket in range(50, 700):
    if ticket not in tickketsid:
        if ticket - 1 in tickketsid and ticket + 1 in tickketsid:
            print(ticket)
