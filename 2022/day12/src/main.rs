use std::collections::HashSet;
use std::collections::VecDeque;
use std::fs;

fn parse(input_folder: &str) -> Vec<Vec<char>> {
    let inputs = fs::read_to_string(input_folder).expect("Unable to read file");

    let parsed_inputs: Vec<Vec<char>> = inputs
        .lines()
        .map(|line| {
            let trimmed = line.trim();
            trimmed.chars().collect()
        })
        .collect();
    parsed_inputs
}

fn get_neighbors(grid: &Vec<Vec<char>>, x: usize, y: usize) -> Vec<(usize, usize)> {
    let current_height = get_height(grid[x][y]);
    let h = grid.len();
    let w = grid[0].len();
    let possible_positions: Vec<(usize, usize)> = vec![(1, 0), (-1, 0), (0, 1), (0, -1)]
        .iter()
        .flat_map(|(i, j)| {
            let new_x = x as i32 + *i;
            let new_y = y as i32 + *j;
            if new_x >= 0 && new_y >= 0 {
                Some((new_x as usize, new_y as usize))
            } else {
                None
            }
        })
        .collect();

    let mut positions = vec![];
    for pos in possible_positions {
        if pos.0 < h && pos.1 < w {
            let position_height = get_height(grid[pos.0][pos.1]);
            if position_height <= current_height + 1 {
                positions.push(pos);
            }
        }
    }
    positions
}

fn get_height(grid_char: char) -> u32 {
    match grid_char {
        'S' => 'a' as u32,
        'E' => 'z' as u32,
        _ => grid_char as u32,
    }
}

fn process(
    grid: &Vec<Vec<char>>,
    start_position: (usize, usize),
    end_position: (usize, usize),
) -> i32 {
    let mut queue = VecDeque::from([(0, start_position)]);
    let mut visited: HashSet<(usize, usize)> = HashSet::new();

    while !queue.is_empty() {
        let (distance, rc) = queue.pop_front().unwrap();
        if rc == end_position {
            return distance;
        }
        if !visited.contains(&rc) {
            visited.insert(rc);
            let neighbors = get_neighbors(grid, rc.0, rc.1);
            for n in neighbors {
                if !visited.contains(&n) {
                    queue.push_back((distance + 1, n));
                }
            }
        }
    }
    i32::MAX
}

fn part_1(grid: &Vec<Vec<char>>) -> Option<i32> {
    let start_position = grid
        .iter()
        .enumerate()
        .find_map(|(i, row)| {
            row.iter().enumerate().find_map(
                |(j, &col)| {
                    if col == 'S' {
                        Some((i, j))
                    } else {
                        None
                    }
                },
            )
        })
        .unwrap();

    let end_position = grid
        .iter()
        .enumerate()
        .find_map(|(i, row)| {
            row.iter().enumerate().find_map(
                |(j, &col)| {
                    if col == 'E' {
                        Some((i, j))
                    } else {
                        None
                    }
                },
            )
        })
        .unwrap();
    let result: i32 = process(grid, start_position, end_position);
    Some(result)
}

fn part_2(grid: &Vec<Vec<char>>) -> Option<i32> {
    let start_positions: Vec<(usize, usize)> = grid
        .iter()
        .enumerate()
        .flat_map(|(i, row)| {
            row.iter().enumerate().filter_map(move |(j, &col)| {
                if col == 'S' || col == 'a' {
                    Some((i, j))
                } else {
                    None
                }
            })
        })
        .collect();

    let end_position = grid
        .iter()
        .enumerate()
        .find_map(|(i, row)| {
            row.iter().enumerate().find_map(
                |(j, &col)| {
                    if col == 'E' {
                        Some((i, j))
                    } else {
                        None
                    }
                },
            )
        })
        .unwrap();
    let mut result = i32::MAX;
    for position in start_positions.iter() {
        let distance = process(grid, *position, end_position);
        if distance < result {
            result = distance;
        }
    }
    Some(result)
}

fn main() {
    let x = parse("input.txt");
    let time = std::time::Instant::now();
    let result_part_1 = part_1(&x).unwrap();
    println!(
        "Result part 1: {:?}, elapsed time: {:?}",
        result_part_1,
        time.elapsed()
    );
    let time_part_2 = std::time::Instant::now();
    let result_part_2 = part_2(&x).unwrap();
    println!(
        "Result part 2: {:?}, elapsed time: {:?}",
        result_part_2,
        time_part_2.elapsed()
    );
}
