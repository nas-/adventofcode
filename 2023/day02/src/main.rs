use std::{collections::HashMap, fs};

#[derive(Debug)]
struct Game {
    blue: i32,
    red: i32,
    green: i32,
}

impl Game {
    fn new(line: &str) -> Self {
        let splitted: Vec<Vec<&str>> = line
            .split(',')
            .map(|f| f.split_ascii_whitespace().collect())
            .collect();
        let mut map: HashMap<&str, i32> = HashMap::new();
        for i in splitted {
            map.insert(i[1], i[0].parse().unwrap());
        }

        Self {
            blue: *map.get("blue").unwrap_or(&0),
            red: *map.get("red").unwrap_or(&0),
            green: *map.get("green").unwrap_or(&0),
        }
    }

    fn possible(&self, other: &Game) -> bool {
        self.blue <= other.blue && self.green <= other.green && self.red <= other.red
    }
}

const BAGCONTENTS: Game = Game {
    blue: 14,
    red: 12,
    green: 13,
};

fn main() {
    let inputs = fs::read_to_string("input").unwrap();
    let cleaned: Vec<Vec<&str>> = inputs
        .split_terminator('\n')
        .map(|f| f.split(':').collect())
        .collect();

    let mut cleaned_inputs: HashMap<i32, Vec<Game>> = HashMap::new();

    for x in cleaned {
        let game_id: i32 = x[0]
            .split_ascii_whitespace()
            .last()
            .unwrap()
            .parse()
            .unwrap();
        let games: Vec<Game> = x[1].split(';').map(Game::new).collect();
        cleaned_inputs.insert(game_id, games);
    }

    println!("part one {:?}", part_one(&cleaned_inputs));
    println!("part two {:?}", part_two(&cleaned_inputs))
}

/// . Filter out impossible games and sum the ids together.
fn part_one(games: &HashMap<i32, Vec<Game>>) -> i32 {
    games
        .iter()
        .filter(|(_, y)| y.iter().all(|k| k.possible(&BAGCONTENTS)))
        .map(|(id, _)| *id)
        .sum()
}

/// . take the max red, blue, green from each set of games, multiply them together.
fn part_two(games: &HashMap<i32, Vec<Game>>) -> i32 {
    games.iter().fold(0, |i, (_, gm)| {
        gm.iter().map(|x| x.red).max().unwrap()
            * gm.iter().map(|x: &Game| x.green).max().unwrap()
            * gm.iter().map(|x| x.blue).max().unwrap()
            + i
    })
}
