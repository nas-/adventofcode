from pathlib import Path

puzzle_input = (Path(__file__).parent / "input").read_text().splitlines()

splitted = []

for x in puzzle_input:
    winning = {a for a in x.split(":")[1].split("|")[0].split(" ") if a != ""}
    have = {b for b in x.split(":")[1].split("|")[1].split(" ") if b != ""}
    splitted.append((winning, have))

sol = 0
for i in splitted:
    intersec = i[0].intersection(i[1])
    if len(intersec) > 0:
        sol += 2 ** (len(intersec) - 1)
print(sol)
