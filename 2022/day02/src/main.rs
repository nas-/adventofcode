use std::fs;
use std::str::Lines;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let split_data = data.lines();
    println!("Result of first part = {}", firstpart(split_data.clone()));
    println!("Result of second part = {}", second_part(split_data))
}

fn second_part(split_data: Lines) -> i32 {
    let mut total = 0;
    for a in split_data {
        let result = generate_score(a.chars().nth(2).expect("Not possible to parse"));
        let theirscore = generate_score(a.chars().nth(0).expect("Not possible to parse"));

        let myscore: i32 = match result {
            2 => theirscore + 3,
            1 => match theirscore {
                1 => 3,
                2 => 1,
                3 => 2,
                _ => -10000,
            },
            3 => match theirscore {
                1 => 2 + 6,
                2 => 3 + 6,
                3 => 1 + 6,
                _ => -10000,
            },
            _ => -10000,
        };
        total += myscore
    }
    total
}

fn firstpart(split_data: Lines) -> i32 {
    let mut total = 0;
    for a in split_data {
        let myscore = generate_score(a.chars().nth(2).expect("Not possible to parse"));
        let theirscore = generate_score(a.chars().nth(0).expect("Not possible to parse"));
        let result: i32;
        if myscore == theirscore {
            result = 3
        } else if (theirscore == 1 && myscore == 3)
            || (theirscore == 2 && myscore == 1)
            || (theirscore == 3 && myscore == 2)
        {
            result = 0
        } else {
            result = 6
        }
        total += myscore + result
    }
    total
}

fn generate_score(score_char: char) -> i32 {
    match score_char {
        'A' | 'X' => 1,
        'B' | 'Y' => 2,
        'C' | 'Z' => 3,
        _ => -1,
    }
}
