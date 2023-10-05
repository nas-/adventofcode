use nom::{
    alt,
    character::complete::{alpha1, digit1},
    delimited, map, named, preceded, separated_list1, tag,
    tuple, verify,
};

named!(label<&str,&str>,verify!(alpha1,|s:&str| {s.len() == 2 && s.chars().all(|c| c.is_ascii_uppercase())}));
named!(valve<&str,&str>,preceded!(tag!("Valve "),label));
named!(flow_rate<&str,u32>,map!(delimited!(tag!(" has flow rate="),digit1,tag!(";")),|s:&str| s.parse::<u32>().unwrap()));
named!(tunnels<&str,Vec<&str>>,preceded!(alt!(tag!(" tunnels lead to valves ")|tag!(" tunnel leads to valve ")),separated_list1!(tag!(", "),label)));
named!(pub line<&str,(&str,u32,Vec<&str>)>,tuple!(valve,flow_rate,tunnels));

#[cfg(test)] // Only compiles when running tests
mod tests {
    use super::*;
    use nom::IResult;

    #[test]
    fn test_valve() {
        let data = "Valve YZ";
        let result: IResult<_, _> = valve(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(parsed_value, "YZ");
            }
            _ => panic!("Unexpected result {:?}", result),
        }
    }

    #[test]
    fn test_flow() {
        let data = " has flow rate=12;";
        let result: IResult<_, _> = flow_rate(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(parsed_value, 12 as u32);
            }
            _ => panic!("Unexpected result {:?}", result),
        }
    }

    #[test]
    fn test_tunnels() {
        let data = " tunnels lead to valves PE, QV, QI, LJ, WX\n";
        let result: IResult<_, _> = tunnels(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(parsed_value, vec!["PE", "QV", "QI", "LJ", "WX"]);
            }
            _ => panic!("Unexpected result {:?}", result),
        }
    }
    #[test]
    fn test_line() {
        let data = "Valve GQ has flow rate=22; tunnels lead to valves SZ, AQ, OW, XJ\n";
        let result: IResult<_, _> = line(data);

        match result {
            Ok((remaining, parsed_value)) => {
                assert_eq!(parsed_value, ("GQ", 22, vec!["SZ", "AQ", "OW", "XJ"]));
            }
            _ => panic!("Unexpected result {:?}", result),
        }
    }
}
