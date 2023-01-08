use std::fs;
use std::str::Lines;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let split_data = data.lines();
    println!("Result of first part = {}", firstpart(split_data))
}

fn firstpart(split_data: Lines) -> i32 {
    let mut total = 0;
    for a in split_data {
        let myscore = generate_score(a.chars().nth(2).expect("Not possible to parse"), false);
        let theirscore = generate_score(a.chars().nth(0).expect("Not possible to parse"), true);
        let mut result = 0;
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

fn generate_score(score_char: char, mine: bool) -> i32 {
    let mut result = 0;
    if mine {
        match score_char {
            'A' => result = 1,
            'B' => result = 2,
            'C' => result = 3,
            _ => println!("anything"),
        }
    } else {
        match score_char {
            'X' => result = 1,
            'Y' => result = 2,
            'Z' => result = 3,
            _ => println!("anything"),
        }
    }
    result
}
