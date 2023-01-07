use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    let split_data = data.lines();

    let mut elves: Vec<i32> = Vec::new();
    let mut cumsum = 0;
    for a in split_data {
        if !a.trim().is_empty() {
            let val_to_sum = a.trim().parse::<i32>().expect("Not possible to parse!");
            cumsum += val_to_sum;
        } else {
            elves.push(cumsum);
            cumsum = 0;
        }
    }

    elves.sort_by(|a, b| b.cmp(a));

    let max_value = elves.iter().max().unwrap();

    let mut sum = 0;
    for el in &elves[0..3] {
        sum += el;
    }

    println!("Part 1 solution: {:?}", max_value);
    println!("Part 2 solution: {:?}", sum);
}
