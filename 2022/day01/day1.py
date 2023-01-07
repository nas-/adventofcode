with open("input.txt") as fin:
    inputs = [jolt.strip() for jolt in fin]

calories = []
cumsum = 0
for n in inputs:
    if n:
        cumsum += int(n)
    else:
        calories.append(cumsum)
        cumsum = 0

print(f"first day answer = {max(calories)}")
print(f"second day answer = {sum(sorted(calories)[-3:])}")
