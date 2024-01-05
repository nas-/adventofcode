use std::{collections::HashMap, fs};

fn main() {
    let inputs = fs::read_to_string("input").unwrap();

    println!("{:?}", part_one(&inputs));
    println!("{:?}", part_two(&inputs));
}

fn part_one(inputs: &str) -> i32 {
    let result_part_one = inputs
        .split_terminator('\n')
        // Filter everything not being a char.
        .map(|f| f.chars().filter(|x| x.is_ascii_digit()).collect())
        // Take first and last number and create number and sum them into accumumlator.
        .fold(0, |acc, element: Vec<char>| {
            let (first, last) = match element.len() {
                0 => ('0', '0'),
                1 => (element[0], element[0]),
                _ => (element[0], *element.last().unwrap()),
            };
            let first_number: i32 = first.to_string().parse().unwrap();
            let last_number: i32 = last.to_string().parse().unwrap();
            acc + first_number * 10 + last_number
        });

    result_part_one
}

fn part_two(inputs: &str) -> i32 {
    let replacements: HashMap<&str, &str> = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]
    .iter()
    .cloned()
    .collect();

    let mut result_part_2 = 0;
    for line in inputs.lines() {
        if let (Some(first_number), Some(second_number)) = (
            clean_line(line, &replacements),
            clean_line_end(line, &replacements),
        ) {
            let num_str: String = format!("{}{}", first_number, second_number);
            let num: i32 = num_str.parse().unwrap_or(0);
            result_part_2 += num;
        }
    }

    result_part_2
}

fn clean_line(line_in: &str, replacements: &HashMap<&str, &str>) -> Option<char> {
    let mut line = line_in;
    while !line.is_empty() {
        if line.chars().next()?.is_ascii_digit() {
            return line.chars().next();
        }
        for (x, replacement) in replacements.iter() {
            if line.starts_with(x) {
                return replacement.chars().next();
            }
        }
        line = &line[1..]
    }
    None
}

fn clean_line_end(line_in: &str, replacements: &HashMap<&str, &str>) -> Option<char> {
    let mut line = line_in;
    while !line.is_empty() {
        if line.chars().next_back()?.is_ascii_digit() {
            return line.chars().next_back();
        }
        for (x, replacement) in replacements.iter() {
            if line.ends_with(x) {
                return replacement.chars().next();
            }
        }
        line = &line[..line.len() - 1]
    }
    None
}
