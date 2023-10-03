use nom::{alt, char, delimited, map, map_opt, named, separated_list0, separated_pair, tag};
use std::cmp::Ordering;
use std::fs;
use std::time::Instant;

fn parse_inputs(input_folder: &str) -> String {
    fs::read_to_string(input_folder).expect("Unable to read file")
}

fn main() {
    let current_time = Instant::now();
    let inputs = parse_inputs("input.txt");
    let part_1 = &inputs
        .split("\r\n\r\n")
        .map(|p| pair(p.as_bytes()).unwrap().1)
        .enumerate()
        .filter(|(_, (a, b))| a.cmp(b) == Ordering::Less)
        .map(|(i, _)| i + 1)
        .sum::<usize>();

    println!("Solution part 1: {:?}", part_1);

    let first = Item::L(vec![Item::L(vec![Item::I(2)])]);
    let second = Item::L(vec![Item::L(vec![Item::I(6)])]);

    let part_2: &mut Vec<Item> = &mut inputs
        .lines()
        .filter(|l| !l.is_empty())
        .map(|p| item(p.as_bytes()).unwrap().1)
        .filter(|i| i < &second)
        .collect();
    part_2.extend([first.clone(), second.clone()]);
    part_2.sort();
    let solution_part_2 = (part_2.iter().position(|i| i == &first).unwrap() + 1)
        * (part_2.iter().position(|i| i == &second).unwrap() + 1);
    println!("Solution part 2: {:?}, completed in {:?} ms", solution_part_2, current_time.elapsed().as_micros())
}

#[derive(PartialEq, Eq, Clone)]
enum Item {
    I(u8),
    L(Vec<Item>),
}

impl Ord for Item {
    fn cmp(&self, other: &Self) -> Ordering {
        match (self, other) {
            (Item::I(a), Item::I(b)) => a.cmp(b),
            (Item::L(a), Item::L(b)) => match a.iter().cmp(b) {
                r if r != Ordering::Equal => r,
                _ => a.len().cmp(&b.len()),
            },
            (Item::I(_), Item::L(b)) if b.len() == 1 => self.cmp(&b[0]),
            (Item::I(a), Item::L(_)) => Item::L(vec![Item::I(*a)]).cmp(other),
            (Item::L(_), Item::I(_)) => other.cmp(self).reverse(),
        }
    }
}

impl PartialOrd for Item {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

named!(item<&[u8], Item>, alt!(map!(list, Item::L) | map!(num, Item::I)));
named!(num<&[u8], u8>, map_opt!(nom::character::complete::digit1, atoi::atoi));
named!(list<&[u8], Vec<Item>>, delimited!(char!('['), separated_list0!(char!(','), item), char!(']')));
named!(pair<&[u8], (Item, Item)>, separated_pair!(item, tag!("\r\n"), item));
