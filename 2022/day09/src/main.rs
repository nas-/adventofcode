use std::collections::HashSet;
use std::fs;

fn parse_inputs() -> Vec<(char, i64)> {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let lines: Vec<(char, i64)> = data
        .lines()
        .map(|line| {
            let parts: Vec<&str> = line.split_whitespace().collect();
            (
                parts[0].parse::<char>().unwrap(),
                parts[1].parse::<i64>().unwrap(),
            )
        })
        .collect();
    lines
}

fn adjust_tail(tail: (i64, i64), head: (i64, i64)) -> (i64, i64) {
    let dx = head.0 - tail.0;
    let dy = head.1 - tail.1;
    match (dx, dy) {
        (dx, dy) if dx.abs() <= 1 && dy.abs() <= 1 => (tail.0, tail.1),
        (0, dy) => (tail.0, tail.1 + dy / dy.abs()),
        (dx, 0) => (tail.0 + dx / dx.abs(), tail.1),
        (dx, dy) => (tail.0 + dx / dx.abs(), tail.1 + dy / dy.abs()),
    }
}

fn part_one(moves: &Vec<(char, i64)>) -> usize {
    let mut tail = (0, 0);
    let mut head = (0, 0);
    let mut tail_visited: HashSet<(i64, i64)> = vec![tail].into_iter().collect();
    for (d, v) in moves {
        for _ in 0..*v {
            let (dx, dy) = match d {
                'U' => (0, 1),
                'D' => (0, -1),
                'R' => (1, 0),
                'L' => (-1, 0),
                _ => panic!("Invalid direction"),
            };
            head = (head.0 + dx, head.1 + dy);
            tail = adjust_tail(tail, head);
            tail_visited.insert(tail);
        }
    }
    tail_visited.len()
}

fn part_2(moves: &Vec<(char, i64)>) -> usize {
    let mut knots = vec![(0, 0); 10];
    let mut tail_visited: HashSet<(i64, i64)> = vec![knots[9]].into_iter().collect();
    for (d, v) in moves {
        for _ in 0..*v {
            let (dx, dy) = match d {
                'U' => (0, 1),
                'D' => (0, -1),
                'R' => (1, 0),
                'L' => (-1, 0),
                _ => panic!("Invalid direction"),
            };
            knots[0] = (knots[0].0 + dx, knots[0].1 + dy);
            for i in 1..knots.len() {
                knots[i] = adjust_tail(knots[i], knots[i - 1]);
            }
            tail_visited.insert(knots[9]);
        }
    }

    tail_visited.len()
}

fn main() {
    let imp = parse_inputs();
    let answer_part_1 = part_one(&imp);
    println!("The answer to part 1 is {}", answer_part_1);
    let answer_part_2 = part_2(&imp);
    println!("The answer to part 2 is {}", answer_part_2);
}
