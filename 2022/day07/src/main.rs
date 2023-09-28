use std::cell::RefCell;
use std::fs;
use std::rc::Rc;

#[derive(Debug, Clone)]
struct Dir {
    _name: String,
    children: Vec<Rc<RefCell<Dir>>>,
    file_size: u64,
}

impl Dir {
    fn new(name: &str) -> Dir {
        Dir {
            _name: name.to_string(),
            children: Vec::<Rc<RefCell<Dir>>>::new(),
            file_size: 0,
        }
    }

    fn size(&self) -> u64 {
        let mut size = self.file_size;
        for child in &self.children {
            size += child.borrow().size();
        }
        size
    }
}

fn parse_inputs() -> Rc<RefCell<Dir>> {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    let root = Rc::new(RefCell::new(Dir {
        _name: String::from("root"),
        children: Vec::new(),
        file_size: 0,
    }));
    let mut current_node = Rc::clone(&root);

    let mut stack = vec![Rc::clone(&root)];

    for input in data.lines() {
        match input {
            string if string.starts_with("$ cd") => {
                let path = string.split(" ").nth(2).unwrap();
                match path {
                    "/" => {
                        current_node = Rc::clone(&root);
                    }
                    ".." => {
                        stack.pop();
                        current_node = Rc::clone(stack.last().unwrap());
                    }
                    path => {
                        let new_node = Rc::new(RefCell::new(Dir::new(path)));
                        current_node
                            .borrow_mut()
                            .children
                            .push(Rc::clone(&new_node));
                        current_node = Rc::clone(&new_node);
                        stack.push(Rc::clone(&new_node));
                    }
                }
            }
            line if line.starts_with("$ ls") => {
                continue;
            }
            line => {
                let tokens = line.split(" ").collect::<Vec<&str>>();
                if tokens[0].starts_with("dir") {
                    let new_node = Rc::new(RefCell::new(Dir::new(tokens[1])));
                    current_node
                        .borrow_mut()
                        .children
                        .push(Rc::clone(&new_node));
                } else {
                    let value = tokens[0].parse::<u64>().unwrap();
                    current_node.borrow_mut().file_size += value;
                }
            }
        }
    }
    root
}

fn compute_directory_sizes(
    root: &Rc<RefCell<Dir>>,
    treshold: u64,
    sizes_list: &Rc<RefCell<Vec<u64>>>,
) -> u64 {
    let mut total_size = 0;

    for child in &root.borrow().children {
        total_size += compute_directory_sizes(child, treshold, sizes_list);
    }

    total_size += root.borrow().file_size;

    if total_size <= treshold {
        sizes_list.borrow_mut().push(total_size);
        return total_size;
    }
    total_size
}

fn find_smallest_directory_to_delete(
    root: &Rc<RefCell<Dir>>,
    free_space: u64,
    required_space: u64,
    to_delete_list: &Rc<RefCell<Vec<u64>>>,
) {
    if free_space + root.borrow().size() >= required_space {
        to_delete_list.borrow_mut().push(root.borrow().size());
    }
    for child in &root.borrow().children {
        find_smallest_directory_to_delete(child, free_space, required_space, to_delete_list);
    }
}

fn main() {
    let current_time = std::time::Instant::now();
    let parsed = parse_inputs();
    let sizes_list = Rc::new(RefCell::new(Vec::<u64>::new()));
    let total_root_size = compute_directory_sizes(&parsed, 100000, &sizes_list);
    println!(
        "The answer to part 1 is {:?}",
        sizes_list.borrow().iter().sum::<u64>()
    );
    let to_delete_list = Rc::new(RefCell::new(Vec::<u64>::new()));
    let total_disk_size = 70000000;
    let required_space = 30000000;
    find_smallest_directory_to_delete(
        &parsed,
        total_disk_size - total_root_size,
        required_space,
        &to_delete_list,
    );
    println!(
        "The answer to part 2 is {:?}",
        to_delete_list.borrow().iter().min().unwrap()
    );
    println!(
        "Time: {}ms",
        current_time.elapsed().as_micros() as f64 / 1000.0
    );
}
