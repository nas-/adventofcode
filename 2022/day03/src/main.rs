use std::collections::HashSet;
use std::fs;
use std::str::Lines;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let split_data = data.lines();
    println!("First part {}", first_part(split_data.clone()));
    println!("Second part {}", second_part(split_data.clone()));
}

fn first_part(split_data: Lines) -> i32 {
    let mut total = 0;
    for line in split_data {
        let (first, second) = line.split_at(line.len() / 2);
        let arr1: Vec<char> = first.chars().collect();
        let arr2: Vec<char> = second.chars().collect();
        let first_set: HashSet<char> = HashSet::from_iter(arr1);
        let second_set: HashSet<char> = HashSet::from_iter(arr2);
        let common = first_set.intersection(&second_set).collect::<HashSet<&char>>();
        for character in common {
            total += get_score(character)
        }
    }
    total
}

fn second_part(split_data: Lines) -> i32 {
    let collected_lines: Vec<&str> = split_data.clone().collect();
    let counter = split_data.count() / 3;
    let mut total = 0;
    for i in 0..counter {
        let arr1: Vec<char> = collected_lines[i * 3].chars().collect();
        let arr2: Vec<char> = collected_lines[(i * 3) + 1].chars().collect();
        let arr3: Vec<char> = collected_lines[(i * 3) + 2].chars().collect();
        let first_set: HashSet<char> = HashSet::from_iter(arr1);
        let second_set: HashSet<char> = HashSet::from_iter(arr2);
        let third_set: HashSet<&char> = HashSet::from_iter(&arr3);
        let common = first_set.intersection(&second_set).collect::<HashSet<&char>>();
        let result = common.intersection(&third_set).collect::<HashSet<&&char>>();
        for character in result {
            total += get_score(character)
        }
    }

    total
}

fn get_score(character: &char) -> i32 {
    return match character {
        'a'..='z' => *character as u8 - 'a' as u8 + 1,
        'A'..='Z' => *character as u8 - 'A' as u8 + 27,
        _ => 0,
    } as i32;
}
