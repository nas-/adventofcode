import re
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sensor:
    x: int
    y: int
    closest_beacon_x: int
    closest_beacon_y: int

    @property
    def min_distance_to_beacon(self):
        return abs(self.x - self.closest_beacon_x) + abs(self.y - self.closest_beacon_y)

    def beacon_can_exist(self, other_x, other_y):
        this_distance = abs(self.x - other_x) + abs(self.y - other_y)

        if this_distance <= self.min_distance_to_beacon:
            return False
        return True

    def distance(self, other_x, other_y):
        return abs(self.x - other_x) + abs(self.y - other_y)


def tuning_frequency(beacon_x, beacon_y):
    return beacon_x * 4000000 + beacon_y


def part_1(sensors, target_row):
    beacon_coords = [(sensor.closest_beacon_x, sensor.closest_beacon_y) for sensor in sensors]
    max_distance = max(sensor.min_distance_to_beacon for sensor in sensors)

    min_x = min(sensor.x for sensor in sensors) - max_distance
    max_x = max(sensor.x for sensor in sensors) + max_distance
    forbittens_positons = []
    for beacon_x in range(min_x, max_x):
        if any(not sensor.beacon_can_exist(beacon_x, target_row) for sensor in sensors):
            if (beacon_x, target_row) not in beacon_coords:
                forbittens_positons.append((beacon_x, target_row))
    return forbittens_positons


def part_2(sensors, max_x):
    part2 = (0, 0)
    in_range = True
    for beacon_y in range(0, max_x + 1):
        beacon_x = 0
        while beacon_x <= max_x:
            pt = (beacon_x, beacon_y)
            in_range = False
            for sensor in sensors:
                if sensor.distance(*pt) <= sensor.min_distance_to_beacon:
                    in_range = True
                    beacon_x = sensor.x + (sensor.min_distance_to_beacon - abs(beacon_y - sensor.y))
                    break
            if not in_range:
                part2 = (beacon_x, beacon_y)
                break
            beacon_x += 1
        if not in_range:
            break
    return part2


if __name__ == "__main__":
    time = datetime.now()
    with open("input.txt") as f:
        data = f.readlines()
    regex = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    sensors = []
    for sensor in data:
        match = regex.match(sensor)
        sensors.append(Sensor(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
    forbittens_positons = part_1(sensors, 2000000)
    print(f"Part 1: {len(forbittens_positons)}, elapsed = {(datetime.now() - time).total_seconds() * 1000}ms")

    possibile_solutions = part_2(sensors, 4000000)
    print(
        f"Part 2: {[tuning_frequency(possibile_solutions[0], possibile_solutions[1])]}, elapsed = {(datetime.now() - time).total_seconds() * 1000}ms")
