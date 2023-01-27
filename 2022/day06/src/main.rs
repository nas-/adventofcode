use ::bounded_vec_deque::BoundedVecDeque;
use std::collections::HashSet;
use std::fs;

fn first_part(data: &str, capacity: usize) -> i32 {
    let mut buffer: BoundedVecDeque<char> = BoundedVecDeque::with_capacity(capacity, capacity);

    for (i, c) in data.chars().enumerate() {
        buffer.push_front(c);
        if buffer.len() == capacity {
            let unique_chars: HashSet<&char> = buffer.iter().collect();
            if unique_chars.len() == capacity {
                return (i + 1) as i32;
            }
        }
    }
    -1
}

fn main() {
    let stri = fs::read_to_string("input.txt").expect("Unable to read file");
    println!("First part: {}", first_part(&stri, 4));
    println!("Second part: {}", first_part(&stri, 14));
}
