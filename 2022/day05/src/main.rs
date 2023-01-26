use std::fs::File;
use std::io::BufReader;
use std::io::Read;
use std::collections::HashMap;


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

    let mut docker = parse_initial_config(initial_config);
    first_part(&mut docker, &moves);
    second_part(&mut docker, &moves);
}

fn first_part(ship_state: &mut HashMap<i32, Vec<char>>, moves: &Vec<Move>) -> () {
    let mut docker = ship_state.clone();
    for mouvement in moves {
        let content = docker.get(&mouvement.from_stack).unwrap();
        let a = content.len() - mouvement.amount as usize;
        let (remaining, to_move) = content.split_at(a);
        let to_stack_value = docker.get(&mouvement.to_stack).unwrap();
        let mut new_value_to_stack = to_stack_value.clone();
        new_value_to_stack.extend(to_move.iter().rev());
        docker.insert(mouvement.from_stack, remaining.clone().to_vec());
        docker.insert(mouvement.to_stack, new_value_to_stack.clone().to_vec());
    }

    let result = collect_result(&mut docker);

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


fn second_part(ship_state: &mut HashMap<i32, Vec<char>>, moves: &Vec<Move>) -> () {
    let mut docker = ship_state.clone();
    for mouvement in moves {
        let content = docker.get(&mouvement.from_stack).unwrap();
        let a = content.len() - mouvement.amount as usize;
        let (remaining, to_move) = content.split_at(a);
        let to_stack_value = docker.get(&mouvement.to_stack).unwrap();
        let mut new_value_to_stack = to_stack_value.clone();
        new_value_to_stack.extend(to_move.iter());
        docker.insert(mouvement.from_stack, remaining.clone().to_vec());
        docker.insert(mouvement.to_stack, new_value_to_stack.clone().to_vec());
    }
    let result = collect_result(&mut docker);

    println!("Second part result {:?}", result);
}


fn parse_initial_config(initial_config: &str) -> HashMap<i32, Vec<char>> {
    let lines = initial_config.split("\n").collect::<Vec<&str>>();
    let mut docker: HashMap<i32, Vec<char>> = HashMap::new();
    let mut indexes: HashMap<i32, i32> = HashMap::new();
    let last_line = lines[lines.len() - 1];
    for (i, c) in last_line.chars().enumerate() {
        if c != ' ' {
            indexes.insert(c.to_digit(10).unwrap() as i32, i as i32);
        }
    }
    for (i, line) in lines.iter().rev().enumerate() {
        if i != 0 {
            for (key, value) in indexes.iter() {
                match line.chars().nth(*value as usize) {
                    Some(' ') => {}
                    Some(val) => {
                        let _ = &docker.entry(*key).or_insert(Vec::new());
                        let curr_value = docker.get_mut(&key).unwrap();
                        curr_value.push(val);
                    },
                    None => {}
                }
            }
        }
    }
    docker
}