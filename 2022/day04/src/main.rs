use std::collections::HashSet;
use std::fs;
use std::str::Lines;


fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let split_data = data.lines();
    println!("First part {}", first_part(split_data.clone()));
    println!("Second part {}", second_part(split_data));
}

fn first_part(split_data: Lines) -> i32 {
    let mut counter = 0;
    for line in split_data {
        let (first_set, second_set) = preprare_sets(line);
        if first_set.is_subset(&second_set) | second_set.is_subset(&first_set) {
            counter += 1
        }
    }
    counter
}

fn second_part(split_data: Lines) -> i32 {
    let mut counter = 0;
    for line in split_data {
        let (first_set, second_set) = preprare_sets(line);
        let intersection: HashSet<_> = first_set.intersection(&second_set).collect::<HashSet<&i32>>();
        if !intersection.is_empty() {
            counter += 1
        }
    }
    counter
}


fn preprare_sets(line: &str) -> (HashSet<i32>, HashSet<i32>) {
    let row = line.split(",").collect::<Vec<&str>>();
    let first = row[0].split('-').collect::<Vec<&str>>();
    let second = row[1].split('-').collect::<Vec<&str>>();
    let first_range: Vec<i32> = make_range(first);
    let second_range: Vec<i32> = make_range(second);
    let first_set: HashSet<i32> = HashSet::from_iter(first_range);
    let second_set: HashSet<i32> = HashSet::from_iter(second_range);
    (first_set, second_set)
}

fn make_range(vector: Vec<&str>) -> Vec<i32> {
    (vector[0].parse::<i32>().unwrap()..vector[1].parse::<i32>().unwrap() + 1 as i32).collect()
}
