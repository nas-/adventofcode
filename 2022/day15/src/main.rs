use regex::Regex;
use std::time::Instant;

#[derive(Debug)]
struct Sensor {
    x: i32,
    y: i32,
    beacon_x: i32,
    beacon_y: i32,
}

impl Sensor {
    fn new(x: i32, y: i32, beacon_x: i32, beacon_y: i32) -> Self {
        Self {
            x,
            y,
            beacon_x,
            beacon_y,
        }
    }

    fn min_distance_to_beacon(&self) -> i32 {
        (self.x - self.beacon_x).abs() + (self.y - self.beacon_y).abs()
    }

    fn distance(&self, x: i32, y: i32) -> i32 {
        (self.x - x).abs() + (self.y - y).abs()
    }

    fn beacon_can_exist(&self, x: i32, y: i32) -> bool {
        self.distance(x, y) > self.min_distance_to_beacon()
    }
}

fn parse_inputs() -> Vec<Sensor> {
    let re =
        Regex::new(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
            .unwrap();
    let input = include_str!("../input.txt");

    let mut sensors = Vec::new();

    for sensor in input.split("\r\n") {
        if let Some(captures) = re.captures(sensor) {
            let sensor = Sensor::new(
                captures[1].parse::<i32>().unwrap(),
                captures[2].parse::<i32>().unwrap(),
                captures[3].parse::<i32>().unwrap(),
                captures[4].parse::<i32>().unwrap(),
            );
            sensors.push(sensor);
        }
    }
    sensors
}

fn part_1(sensors: &[Sensor], target_row: i32) -> Vec<(i32, i32)> {
    let beacon_coordinated: Vec<(i32, i32)> = sensors
        .iter()
        .map(|sensor| (sensor.beacon_x, sensor.beacon_y))
        .collect();
    let max_distance: i32 = sensors
        .iter()
        .map(|sensor| sensor.min_distance_to_beacon())
        .max()
        .unwrap();
    let min_x = sensors.iter().map(|x| x.x).min().unwrap() - max_distance;
    let max_x = sensors.iter().map(|x| x.x).max().unwrap() + max_distance;
    let mut forbidden_positons = vec![];

    for beacon_x in min_x..max_x + 1 {
        if sensors
            .iter()
            .any(|sensor| !sensor.beacon_can_exist(beacon_x, target_row))
            && !beacon_coordinated.contains(&(beacon_x, target_row))
        {
            forbidden_positons.push((beacon_x, target_row));
        }
    }
    forbidden_positons
}

fn part_2(sensors: &Vec<Sensor>, max_size: i32) -> (i32, i32) {
    let mut part_2_result = (0, 0);
    let mut in_range = true;

    for beacon_y in 0..max_size + 1 {
        let mut beacon_x = 0;
        while beacon_x <= max_size {
            in_range = false;
            for sensor in sensors {
                if sensor.distance(beacon_x, beacon_y) <= sensor.min_distance_to_beacon() {
                    in_range = true;
                    beacon_x =
                        sensor.x + (sensor.min_distance_to_beacon() - (beacon_y - sensor.y).abs());
                    break;
                }
            }
            if !in_range {
                part_2_result = (beacon_x, beacon_y);
                break;
            }
            beacon_x += 1;
        }
        if !in_range {
            break;
        }
    }
    part_2_result
}

fn tuning_frequency(x: i32, y: i32) -> i64 {
    x as i64 * 4000000 + y as i64
}

fn main() {
    let time = Instant::now();
    let sensors = parse_inputs();
    let part_1 = part_1(&sensors, 2000000);
    println!(
        "Part 1 result: {:?}, elapsed {:?}",
        part_1.len(),
        time.elapsed().as_millis()
    );
    let part_2 = part_2(&sensors, 4000000);
    let part_2_res = tuning_frequency(part_2.0, part_2.1);
    println!(
        "Part 2 result: {:?}, elapsed {:?}",
        part_2_res,
        time.elapsed().as_millis()
    );
}
