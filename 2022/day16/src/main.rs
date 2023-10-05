use crate::parser::line;
use itertools::Itertools;
use std::collections::HashMap;
use std::time::Instant;
mod parser;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct ParsedLine<'a> {
    label: &'a str,
    flow: u32,
    leads_to: Vec<&'a str>,
}

impl Ord for ParsedLine<'_> {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.label.cmp(other.label)
    }
}

impl PartialOrd for ParsedLine<'_> {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Valve {
    pub id: u64,
    pub flow: u32,
}

impl Valve {
    fn new(id: u64, flow: u32) -> Self {
        Self { id, flow }
    }
}

struct ValveMap {
    edges: Vec<Vec<(usize, u32)>>,
    valves: Vec<Valve>,
}

impl From<Vec<ParsedLine<'_>>> for ValveMap {
    fn from(value: Vec<ParsedLine>) -> Self {
        let mut nodes = Vec::new();
        for (idx, entry) in value.iter().enumerate() {
            let id = 2u64.pow(idx as u32);
            let flow = entry.flow;
            let valve = Valve::new(id, flow);
            nodes.push(valve);
        }
        let label_idx_map = value
            .iter()
            .enumerate()
            .map(|(idx, entry)| (entry.label, idx))
            .collect::<HashMap<_, _>>();

        let mut dist_matrix = vec![vec![u32::MAX; value.len()]; value.len()];
        for (idx, entry) in value.iter().enumerate() {
            dist_matrix[idx][idx] = 0;
            for neighbor in entry.leads_to.iter() {
                let neighbor_idx = label_idx_map[neighbor];
                dist_matrix[idx][neighbor_idx] = 1;
            }
        }

        for permutation in (0..value.len()).permutations(3) {
            let (k, i, j) = (permutation[0], permutation[1], permutation[2]);
            let detour_dist = dist_matrix[i][k].saturating_add(dist_matrix[k][j]);
            if detour_dist < dist_matrix[i][j] {
                dist_matrix[i][j] = detour_dist;
            }
        }

        let mut edges = Vec::new();
        for (start, _) in nodes.iter().enumerate() {
            let mut edges_from = Vec::new();
            for (end, end_valve) in nodes.iter().enumerate() {
                if start == end || end_valve.flow == 0 {
                    continue;
                }
                edges_from.push((end, dist_matrix[start][end]));
            }

            edges.push(edges_from);
        }
        ValveMap {
            edges,
            valves: nodes,
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct TravelState {
    pub location: usize,
    pub valves_open: u64,
    pub remaining: u32,
    pub released: u32,
}

impl Default for TravelState {
    fn default() -> Self {
        TravelState {
            location: Default::default(),
            valves_open: Default::default(),
            remaining: 30, // Default to 30 minutes remaining
            released: Default::default(),
        }
    }
}
impl TravelState {
    fn next_states(&self, map: &ValveMap) -> Vec<TravelState> {
        let mut out = Vec::new();

        for (neighbor, distance) in map.edges[self.location].iter() {
            if *distance >= self.remaining {
                continue;
            }
            let valve = map.valves[*neighbor];
            if valve.id & self.valves_open > 0 {
                continue;
            }

            let mut new_state = *self;
            new_state.location = *neighbor;
            new_state.valves_open |= valve.id;
            new_state.remaining -= distance + 1;
            new_state.released += new_state.remaining * valve.flow;
            out.push(new_state);
        }
        if out.is_empty() {
            let mut wait_state = *self;
            wait_state.remaining = 0;
            out.push(wait_state)
        }

        out
    }
}
impl Ord for TravelState {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.released.cmp(&other.released)
    }
}

impl PartialOrd for TravelState {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

fn part_1(input: &ValveMap) -> u32 {
    let state = TravelState::default();
    let mut open = vec![state];

    let mut max_released = 0;

    while let Some(state) = open.pop() {
        if state.remaining == 0 {
            max_released = max_released.max(state.released);
            continue;
        }

        for next_state in state.next_states(input) {
            open.push(next_state);
        }
    }

    max_released.into()
}

fn part_2(input: &ValveMap) -> u32 {
    let state = TravelState {
        remaining: 26,
        ..Default::default()
    };
    let mut open = vec![state];

    let mut best_results = Vec::new();
    while let Some(state) = open.pop() {
        if state.remaining == 0 {
            best_results.push(state);
            continue;
        }

        for neighbor in state.next_states(input) {
            open.push(neighbor);
        }
    }

    best_results.sort_unstable();

    for (idx, result1) in best_results.iter().rev().enumerate() {
        for result2 in best_results.iter().rev().skip(idx + 1) {
            if result1.valves_open & result2.valves_open > 0 {
                continue;
            }
            let max = result1.released + result2.released;
            return max;
        }
    }

    panic!("Could not solve part two!");
}

fn main() {
    let time = Instant::now();
    let input = include_str!("../input.txt");
    let mut lines: Vec<ParsedLine> = input
        .split_terminator('\n')
        .map(|l| line(l).unwrap().1)
        .map(|(a, b, c)| ParsedLine {
            label: a,
            flow: b,
            leads_to: c,
        })
        .collect();
    // Sort the lines by label, AA is the starting point
    lines.sort_unstable();
    let valve_map = ValveMap::from(lines);
    let result = part_1(&valve_map);
    println!(
        "Part 1 solution: {}, took {:?} ms",
        result,
        time.elapsed().as_millis()
    );
    let result2 = part_2(&valve_map);
    println!(
        "Part 2 solution: {}, took {:?} ms",
        result2,
        time.elapsed().as_millis()
    );
}
