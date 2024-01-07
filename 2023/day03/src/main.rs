use std::fs;

fn main() {
    let inputs: Vec<Vec<char>> = fs::read_to_string("input")
        .unwrap()
        .split_terminator('\n')
        .map(|f| f.chars().collect())
        .collect();
    println!("part one {:?}", part_one(&inputs));
}

fn is_valid(x: usize, y: usize, grid: &Vec<Vec<char>>) -> bool {
    x < grid.len() && y < grid[0].len()
}

fn check_neightbours(grid: &Vec<Vec<char>>, x: usize, y: usize) -> bool {
    let places = [
        (x + 1, y),
        (x.checked_sub(1).unwrap_or(x), y),
        (x, y + 1),
        (x, y.checked_sub(1).unwrap_or(y)),
        (x + 1, y + 1),
        (x + 1, y.checked_sub(1).unwrap_or(y)),
        (x.checked_sub(1).unwrap_or(x), y + 1),
        (x.checked_sub(1).unwrap_or(x), y.checked_sub(1).unwrap_or(y)),
    ];
    for place in places.iter() {
        if !is_valid(place.0, place.1, grid) {
            continue;
        }
        let el = grid[place.0][place.1];
        if el != '.' && !el.is_ascii_digit() {
            return true;
        }
    }
    false
}

fn part_one(grid: &Vec<Vec<char>>) -> i32 {
    let mut solution_part_1 = 0;
    for row in 0..grid.len() {
        let mut number: String = "".to_owned();
        let mut valid = false;
        for col in 0..grid[0].len() {
            let el = grid[row][col];
            if el.is_ascii_digit() {
                number = format!("{number}{el}");
                let valid_position = check_neightbours(grid, row, col);
                if valid_position {
                    valid = true;
                }
            } else {
                if number != *"" && valid {
                    solution_part_1 += number.parse::<i32>().unwrap();
                }
                number = "".to_owned();
                valid = false;
            }
        }
        if number != *"" && valid {
            solution_part_1 += number.parse::<i32>().unwrap();
        }
    }
    solution_part_1
}
