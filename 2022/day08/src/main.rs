use std::collections::HashMap;
use std::fs;

fn parse_inputs() -> Vec<Vec<i32>> {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let lines: Vec<Vec<char>> = data
        .lines()
        .map(|line| line.trim().chars().collect())
        .collect();

    let mut grid: Vec<Vec<i32>> = Vec::new();
    for line in lines.iter() {
        let mut row: Vec<i32> = Vec::new();
        for ch in line.iter() {
            let num = ch.to_digit(10).unwrap() as i32;
            row.push(num);
        }
        grid.push(row);
    }
    grid
}

fn is_visible(i: usize, j: usize, grid: &Vec<Vec<i32>>) -> bool {
    let element = grid[i][j];
    let mut visibility_map = HashMap::from([
        ("left", false),
        ("right", false),
        ("top", false),
        ("down", false),
    ]);
    let mut is_edge = false;
    if i == 0 {
        visibility_map.insert("top", true);
        is_edge = true;
    }
    if i == grid.len() - 1 {
        visibility_map.insert("down", true);
        is_edge = true;
    }
    if j == 0 {
        visibility_map.insert("left", true);
        is_edge = true;
    }
    if j == grid[0].len() - 1 {
        visibility_map.insert("right", true);
        is_edge = true;
    }
    if is_edge == false {
        let row = &grid[i as usize];
        let column = grid.iter().map(|row| row[j as usize]).collect::<Vec<i32>>();
        let visibility_left = (0..j).all(|k| element > row[k as usize]);
        visibility_map.insert("left", visibility_left);
        let visibility_right = (j + 1..row.len()).all(|w| element > row[w as usize]);
        visibility_map.insert("right", visibility_right);
        let visibility_top = (0..i).all(|k| element > column[k as usize]);
        visibility_map.insert("top", visibility_top);
        let visibility_down = (i + 1..column.len()).all(|w| element > column[w as usize]);
        visibility_map.insert("down", visibility_down);
    }
    visibility_map.values().any(|&x| x == true)
}

fn part_1(grid: &Vec<Vec<i32>>) -> i32 {
    let mut count = 0;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if is_visible(i, j, grid) {
                count += 1;
            }
        }
    }
    count
}

fn can_see_trees_in_direction(
    grid: &Vec<Vec<i32>>,
    row: usize,
    col: usize,
    dr: i32,
    dc: i32,
) -> i32 {
    let height = grid[row][col];
    let mut distance = 0;
    let mut row = row as i32;
    let mut col = col as i32;
    loop {
        row += dr as i32;
        col += dc as i32;
        if (0 <= row && row < grid.len() as i32 && 0 <= col && col < grid[0].len() as i32) == false
        {
            return distance;
        }
        if grid[row as usize][col as usize] < height {
            distance += 1;
        } else {
            return distance + 1;
        }
    }
}

fn scenic_score(grid: &Vec<Vec<i32>>, row: usize, col: usize) -> i32 {
    let up = can_see_trees_in_direction(&grid, row, col, -1, 0);
    let left = can_see_trees_in_direction(&grid, row, col, 0, -1);
    let right = can_see_trees_in_direction(&grid, row, col, 0, 1);
    let down = can_see_trees_in_direction(&grid, row, col, 1, 0);
    up * left * right * down
}

fn highest_scenic_score(grid: &Vec<Vec<i32>>) -> i32 {
    let mut highest_score = 0;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            let scenic_score = scenic_score(&grid, i, j);
            if scenic_score > highest_score {
                highest_score = scenic_score;
            }
        }
    }
    highest_score
}

fn main() {
    let current_time = std::time::Instant::now();
    let grid = parse_inputs();
    let answer = part_1(&grid);
    println!("The answer to part 1 is {}", answer);
    let answer_part_2 = highest_scenic_score(&grid);
    println!("The answer to part 2 is {}", answer_part_2);
    println!(
        "Elapsed time: {:.2?}",
        std::time::Instant::now().duration_since(current_time)
    );
}
