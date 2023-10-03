use nom::{char, map_opt, named, separated_list1, separated_pair};
use std::time::Instant;

const W: usize = 665;
const H: usize = 165;

fn main() {
    let time = Instant::now();

    let (mut map, mut sand, _) = generate_grid();

    while let Some((x, y)) = trace(&map, (500, 0)) {
        map[y][x] = true;
        sand += 1;
    }

    println!(
        "Part 1 solution: {}, took {:?} ms",
        sand,
        time.elapsed().as_millis()
    );

    let (mut map_2, mut sand_2, lowest) = generate_grid();

    while let Some((x, y)) = trace2(&map_2, (500, 0), lowest + 2) {
        sand_2 += 1;
        map_2[y][x] = true;
        if y == 0 {
            break;
        }
    }

    println!(
        "Part 2 solution: {}, took {:?} ms",
        sand_2,
        time.elapsed().as_millis()
    );
}

fn generate_grid() -> ([[bool; 665]; 165], i32, usize) {
    let (mut map, sand) = ([[false; W]; H], 0);
    let mut lowest = 0;
    include_bytes!("../input.txt")
        .split(|b| b == &b'\n')
        .filter(|l| !l.is_empty())
        .map(|p| line(p).unwrap().1)
        .for_each(|coord| {
            coord.windows(2).for_each(|pair| {
                if let [a, b] = pair {
                    lowest = lowest.max(a.1.max(b.1));
                    if a.0 == b.0 {
                        // Vertical line
                        (a.1.min(b.1)..=a.1.max(b.1)).for_each(|y| map[y][a.0] = true);
                    } else {
                        // Horizontal line
                        (a.0.min(b.0)..=a.0.max(b.0)).for_each(|x| map[a.1][x] = true);
                    }
                }
            })
        });
    (map, sand, lowest)
}

fn trace2(map: &[[bool; W]; H], (mut x, y): (usize, usize), low: usize) -> Option<(usize, usize)> {
    (y..H - 1)
        .find(|y| {
            *y == low - 1
                || [x, x - 1, x + 1]
                    .into_iter()
                    .find(|x| !map[*y + 1][*x])
                    .map(|xx| x = xx)
                    .is_none()
        })
        .map(|y| (x, y))
}

fn trace(map: &[[bool; W]; H], (mut x, y): (usize, usize)) -> Option<(usize, usize)> {
    (y + 1..H - 1)
        .find(|y| {
            [x, x - 1, x + 1]
                .into_iter()
                .find(|x| !map[*y + 1][*x])
                .map(|xx| x = xx)
                .is_none()
        })
        .map(|y| (x, y))
}

named!(usize<&[u8], usize>,map_opt!(nom::character::complete::digit1,atoi::atoi));
named!(coordinates<&[u8], (usize,usize)>,separated_pair!(usize,char!(','),usize));
named!(line<&[u8], Vec<(usize,usize)>>, separated_list1!(nom::bytes::complete::tag(" -> "),coordinates));

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::*;
    use nom::{
        character::complete::digit1, combinator::map_opt, error::ErrorKind, Finish, IResult,
    };

    #[test]
    fn test_usize() {
        let data = b"123";
        let result: IResult<_, _> = usize(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(remaining, &b""[..]);
                assert_eq!(parsed_value, 123);
            }
            _ => panic!("Unexpected result {:?}", result),
        }
    }

    #[test]
    fn test_coordinates() {
        let data = b"123,124";
        let result: IResult<_, _> = coordinates(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(remaining, &b""[..]);
                assert_eq!(parsed_value, (123, 124));
            }
            _ => {
                panic!("Unexpected result {:?}", result);
            }
        }
    }

    #[test]
    fn test_line() {
        let data = b"123,124 -> 232,234";
        let result: IResult<_, _> = line(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(remaining, &b""[..]);
                assert_eq!(parsed_value, vec![(123, 124), (232, 234)]);
            }
            _ => {
                panic!("Unexpected result {:?}", result);
            }
        }
    }
}
