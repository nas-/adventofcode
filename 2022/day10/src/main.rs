use std::collections::HashMap;
use std::fs;

fn parse_inputs() -> Vec<Vec<String>> {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let lines: Vec<Vec<String>> = data
        .lines()
        .map(|x| {
            let trimmed = x.trim();
            trimmed.split_whitespace().map(|x| x.to_string()).collect()
        })
        .collect();
    lines
}

fn part_1(inputs: &[Vec<String>]) -> HashMap<i64, i64> {
    let mut cycle_number: i64 = 1;
    let mut registry_value = 1;
    let mut cycle_values = HashMap::from([(cycle_number, registry_value)]);

    for i in inputs.iter() {
        match i {
            i if i.get(0).unwrap() == &"addx".to_string() => {
                cycle_number += 1;
                cycle_values.insert(cycle_number, registry_value);
                cycle_number += 1;
                registry_value += i.get(1).unwrap().parse::<i64>().unwrap();
            }
            i if i.get(0).unwrap() == &"noop".to_string() => {
                cycle_number += 1;
            }
            _ => {}
        }
        cycle_values.insert(cycle_number, registry_value);
    }
    cycle_values
}

fn part_2(inputs: &HashMap<i64, i64>) {
    let mut drawn = vec![];
    for position in 0..240 {
        let cycle = position + 1;
        let register_val = inputs.get(&cycle).unwrap();
        let condition = position % 40 - register_val;
        if (-1..=1).contains(&condition) {
            drawn.push(position);
        }
    }
    for k in 0..6 {
        for i in 0..40 {
            if drawn.contains(&((i + k * 40) as i64)) {
                print!("*");
            } else {
                print!(" ");
            }
        }
        println!();
    }
}

fn main() {
    let current_time = std::time::Instant::now();
    let inputs = parse_inputs();
    let mymap: HashMap<i64, i64> = part_1(&inputs);
    let values_to_check = vec![20, 60, 100, 140, 180, 220];
    let result_part_1: i64 = mymap
        .iter()
        .filter(|(k, _)| values_to_check.contains(k))
        .map(|(k, v)| k * v)
        .sum();

    println!("Result part 1: {:?}", result_part_1);
    println!("Result part 2:");
    part_2(&mymap);
    println!("Elapsed time: {:?}", current_time.elapsed());
}
