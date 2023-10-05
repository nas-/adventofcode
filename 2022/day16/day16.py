import re
from dataclasses import dataclass, field
from datetime import datetime
from itertools import permutations


@dataclass
class TravelState:
    location: int
    valves_open: field(default_factory=list)
    remaining: int
    released: int

    def next_states(self, edges, nodes):
        out = []
        for neighbor, distance in edges[self.location]:
            if distance >= self.remaining:
                continue
            valve = nodes[neighbor]
            if valve.id in self.valves_open:
                continue

            valves_open = self.valves_open.copy()
            valves_open.append(valve.id)
            loc = neighbor
            time_remaining = self.remaining - (distance + 1)
            flow = self.released + (time_remaining * valve.rate)
            out.append(TravelState(loc, valves_open, time_remaining, flow))

        if not out:
            out.append(TravelState(self.location, self.valves_open, 0, self.released))
        return out


@dataclass
class Valve:
    name: str
    rate: int
    tunnels: field(default_factory=list)
    id: field(init=False)


def parse_input():
    with open("input.txt") as f:
        data = f.readlines()
    regex = re.compile(
        r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)"
    )
    valves = []
    for i, valve_str in enumerate(data):
        match = regex.match(valve_str)
        valve = Valve(
            name=match.groups()[0],
            rate=int(match.groups()[1]),
            tunnels=[x.strip() for x in match.groups()[2].split(",")],
            id=i,
        )
        valves.append(valve)

    label_idx_map = {valve.name: i for i, valve in enumerate(valves)}
    grid = [[float("inf") for _ in range(len(valves))] for _ in range(len(valves))]
    for i, v in enumerate(valves):
        v.id = label_idx_map[v.name]
        grid[i][i] = 0
        for neighbor in v.tunnels:
            grid[i][label_idx_map[neighbor]] = 1

    for k, i, j in permutations(range(len(valves)), 3):
        detur_dist = grid[i][k] + grid[k][j]
        if detur_dist < grid[i][j]:
            grid[i][j] = detur_dist

    edges = []
    for start, start_valve in enumerate(valves):
        edges_from = []
        for end, end_valve in enumerate(valves):
            if start_valve == end_valve or end_valve.rate == 0:
                continue
            edges_from.append((end, grid[start][end]))
        edges.append(edges_from)

    return valves, edges


def part_1(valves, edges):
    state_where_AA_is = [i for i, valve in enumerate(valves) if valve.name == "AA"][0]
    state = TravelState(state_where_AA_is, [], 30, 0)
    opened = [state]
    max_released = 0

    while opened:
        internal_state = opened.pop()
        if internal_state.remaining == 0:
            max_released = max(max_released, internal_state.released)
            continue
        for next_state in internal_state.next_states(edges, valves):
            opened.append(next_state)

    return max_released


def part_2(valves, edges):
    state_where_AA_is = [i for i, valve in enumerate(valves) if valve.name == "AA"][0]
    state = TravelState(state_where_AA_is, [], 26, 0)
    opened = [state]
    end_states = []

    while opened:
        internal_state = opened.pop()
        if internal_state.remaining == 0:
            end_states.append(internal_state)
            continue
        for next_state in internal_state.next_states(edges, valves):
            opened.append(next_state)

    new_end_states = sorted(end_states, key=lambda x: x.released, reverse=True)
    for i, result1 in enumerate(new_end_states):
        for result2 in new_end_states:
            if any(valve_id in result1.valves_open for valve_id in result2.valves_open):
                continue
            max = result1.released + result2.released
            return max
    raise Exception("No result found")


if __name__ == "__main__":
    start_time = datetime.now()
    inputs, edges = parse_input()
    part_1_res = part_1(inputs, edges)
    print(
        f"Part 1: {part_1_res}, elapsed: {(datetime.now() - start_time).total_seconds() * 1000}ms"
    )
    part_2_res = part_2(inputs, edges)
    print(
        f"Part 2: {part_2_res}, elapsed: {(datetime.now() - start_time).total_seconds() * 1000}ms"
    )
