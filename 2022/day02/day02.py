with open("input.txt") as fin:
    inputs = [jolt.strip() for jolt in fin]

MYSCORES = ["", "X", "Y", "Z"]
THEIR = "0ABC"
CONDITIONS = ["lose", "draw", "win"]
total = 0
for i in inputs:
    my_score = MYSCORES.index(i[-1])
    theirscore = THEIR.index(i[0])
    if my_score == theirscore:
        result = 3
    elif (
            theirscore == 1
            and my_score == 3
            or theirscore == 2
            and my_score == 1
            or theirscore == 3
            and my_score == 2
    ):  # rock
        result = 0
    else:
        result = 6
    total += my_score + result

print(f"first part total: {total}")

total_part_2 = 0
for i in inputs:
    result = MYSCORES.index(i[-1])
    theirscore = THEIR.index(i[0])
    if result == 2:
        myscore = theirscore + 3
    elif result == 1:  # lose
        if theirscore == 1:
            myscore = 3
        elif theirscore == 2:
            myscore = 1
        elif theirscore == 3:
            myscore = 2
    else:
        if theirscore == 1:
            myscore = 2 + 6
        elif theirscore == 2:
            myscore = 3 + 6
        elif theirscore == 3:
            myscore = 1 + 6
    total_part_2 += myscore

print(f"Second part total: {total_part_2}")
