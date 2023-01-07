import functools

with open("input.txt") as fin:
    instructions = [int(jolt.strip()) for jolt in fin]

instructions.append(0)
instructions.append(max(instructions) + 3)

B = sorted(instructions)

joltageDiffs = []
for index, element in enumerate(B):
    if index >= len(B) - 1:
        continue
    joltage = B[index + 1] - element
    joltageDiffs.append(joltage)

print(f"Part1 :{joltageDiffs.count(3) * joltageDiffs.count(1)}")


@functools.lru_cache(128)
def get_ways(i):
    if i == len(B) - 1:
        return 1
    return sum(get_ways(j) for j in range(i + 1, len(B)) if B[j] - B[i] <= 3)


print(f"Part 2: {get_ways(0)}")

# def dp(i):
#     if i == len(instructions) - 1:
#         return 1
#     if i in DP:
#         return DP[i]
#     ans = 0
#     for j in range(i + 1, len(xs)):
#         if xs[j] - xs[i] <= 3:
#             # one way to get from i to the end is to first step to j
#             # the number of paths from i that *start* by stepping to xs[j] is just DP[j]
#             # So dp(i) = \sum_{valid j} dp(j)
#             ans += dp(j)
#     DP[i] = ans
#     return ans
