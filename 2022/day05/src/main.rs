use std::collections::HashMap;
use std::fs::File;
use std::io::BufReader;
use std::io::Read;

#[derive(Debug)]
struct Move {
    amount: i32,
    from_stack: i32,
    to_stack: i32,
}

impl Move {
    fn from_line(line: &str) -> Self {
        let split_line: Vec<&str> = line.split_whitespace().collect();
        Move {
            amount: split_line[1].parse().unwrap(),
            from_stack: split_line[3].parse().unwrap(),
            to_stack: split_line[5].parse().unwrap(),
        }
    }
}

fn main() {
    let file = File::open("input.txt").unwrap();
    let mut reader = BufReader::new(file);
    let mut inputs = String::new();
    reader.read_to_string(&mut inputs).unwrap();
    inputs = inputs.replace("\r\n", "\n");
    let (initial_config, commands) = inputs.split_once("\n\n").unwrap();
    let command_list: Vec<&str> = commands.split("\n").collect();

    let mut moves: Vec<Move> = Vec::new();
    for line in command_list {
        moves.push(Move::from_line(line))
    }

    let docker = parse_initial_config(initial_config);
    first_part(&mut docker.clone(), &moves);
    second_part(&mut docker.clone(), &moves);
}

fn first_part(ship_state: &mut HashMap<i32, Vec<char>>, moves: &Vec<Move>) -> () {
    for movement in moves {
        let from_stack = ship_state.get_mut(&movement.from_stack).unwrap();
        let amount = movement.amount as usize;
        let to_move = from_stack.split_off(from_stack.len() - amount);
        let to_stack = ship_state.get_mut(&movement.to_stack).unwrap();
        to_stack.extend(to_move.iter().rev());
    }
    let result = collect_result(ship_state);

    println!("First part {:?}", result);
}

fn collect_result(docker: &mut HashMap<i32, Vec<char>>) -> String {
    let mut keys: Vec<&i32> = docker.keys().collect();
    keys.sort();

    let mut result = String::new();
    for i in keys {
        let last_char = docker[i].last().unwrap();
        result.push(*last_char);
    }
    result
}

fn second_part(ship_state: &mut HashMap<i32, Vec<char>>, moves: &Vec<Move>) {
    for movement in moves {
        let from_stack = ship_state.get_mut(&movement.from_stack).unwrap();
        let amount = movement.amount as usize;
        let to_move = from_stack.split_off(from_stack.len() - amount);
        let to_stack = ship_state.get_mut(&movement.to_stack).unwrap();
        to_stack.extend(to_move.iter());
    }
    let result = collect_result(ship_state);

    println!("Second part result {:?}", result);
}

fn parse_initial_config(initial_config: &str) -> HashMap<i32, Vec<char>> {
    let lines = initial_config.split("\n").collect::<Vec<&str>>();
    let mut docker: HashMap<i32, Vec<char>> = HashMap::new();
    let last_line = lines[lines.len() - 1];
    let indexes = last_line
        .chars()
        .enumerate()
        .filter(|(_, c)| *c != ' ')
        .map(|(i, c)| (c.to_digit(10).unwrap() as i32, i as i32))
        .collect::<HashMap<i32, i32>>();

    for (_, line) in lines.iter().rev().enumerate().filter(|(i, _)| *i != 0) {
        for (key, value) in indexes.iter() {
            match line.chars().nth(*value as usize) {
                Some(' ') => {}
                Some(val) => {
                    docker.entry(*key).or_default().push(val);
                }
                None => {}
            }
        }
    }
    docker
}
