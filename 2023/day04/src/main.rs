use std::{collections::HashSet, fs, time::Instant};

fn main() {
    let inputs = fs::read_to_string("input").unwrap();
    let base = inputs.split_terminator('\n').collect();
    let time = Instant::now();
    let part_one = part_one(&base);
    let elapsed = time.elapsed().as_millis();
    println!("Result part one {} needed {} ms", part_one, elapsed)
}

fn part_one(cards: &Vec<&str>) -> i32 {
    let mut splitted: Vec<(HashSet<&str>, HashSet<&str>)> = vec![];
    for card in cards.iter() {
        let winning: HashSet<&str> = HashSet::from_iter(
            card.split(':')
                .nth(1)
                .unwrap()
                .split('|')
                .next()
                .unwrap()
                .split(' ')
                .filter(|&a| !a.is_empty()),
        );
        let have: HashSet<&str> = HashSet::from_iter(
            card.split(':')
                .nth(1)
                .unwrap()
                .split('|')
                .nth(1)
                .unwrap()
                .split(' ')
                .filter(|&a| !a.is_empty()),
        );
        splitted.push((winning, have))
    }
    let mut sol: i32 = 0;
    for i in splitted.iter() {
        let intersec: HashSet<&str> = i.0.intersection(&i.1).cloned().collect();
        if !intersec.is_empty() {
            sol += 2_i32.pow((intersec.len() - 1).try_into().unwrap())
        }
    }
    sol
}
