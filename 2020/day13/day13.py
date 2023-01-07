fin = open("input.txt")

data = [data.strip() for data in fin.readlines()]
earliest_time = int(data[0])
busses = data[1].split(",")

index = earliest_time
unfound = True
busID = 0
while unfound:
    index += 1
    for bus in busses:
        if bus == "x":
            continue
        bus = int(bus)
        if index % bus == 0:
            unfound = False
            busID = bus
            break

print(f"Part 1: {(index - earliest_time) * busID}")

a = set(busses.copy())
a.remove("x")
setss = sorted(list(set(map(int, a))))

jump = setss[0]
index_2 = 0
for element in setss[1:]:
    while (index_2 + busses.index(str(element))) % element != 0:
        index_2 += jump
    jump *= element
print(f"Part 2: {index_2}")
