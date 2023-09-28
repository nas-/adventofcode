class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, entry):
        self.contents.append(entry)

    @property
    def size(self):
        return sum([entry.size for entry in self.contents])


def parse_input(inputs: str):
    root = Directory("/")
    current_dir = root
    stack = [root]

    commands = inputs.split(r"$")
    for command in commands:
        stripped = command.strip()
        if stripped.startswith("cd"):
            splitted = stripped.split(" ")
            if splitted[1] == "..":
                stack.pop()
                current_dir = stack[-1]
            elif splitted[1].startswith("/"):
                current_dir = root
                stack = [root]
            else:
                new_dir = Directory(splitted[1])
                current_dir.add(new_dir)
                current_dir = new_dir
                stack.append(new_dir)
        elif stripped.startswith("ls"):
            results = [res.strip() for res in stripped.split("\n")][1:]
            for result in results:
                tokents = result.split(" ")
                if tokents[0] == "dir":
                    current_dir.add(Directory(tokents[1]))
                else:
                    current_dir.add(File(tokents[1], int(tokents[0])))
    return root


def compute_directory_sizes(node, size_dict: list, treshold: int) -> list:
    if isinstance(node, Directory):
        if node.size <= treshold:
            size_dict.append(node.size)
        for entry in node.contents:
            compute_directory_sizes(entry, size_dict, treshold)
    return size_dict


def find_smallest_directory_to_delete(node, free_space, required_space, sizes):
    if isinstance(node, Directory):
        if free_space + node.size >= required_space:
            sizes.append(node.size)
        for entry in node.contents:
            if isinstance(entry, Directory):
                find_smallest_directory_to_delete(
                    entry, free_space, required_space, sizes=sizes
                )
    return sizes


if __name__ == "__main__":
    with open("input.txt") as fin:
        inputs = parse_input(fin.read().strip())
    size_dict = compute_directory_sizes(inputs, [], 100000)
    print(sum(size_dict))
    total_disk_space = 70000000
    required_space = 30000000
    k = find_smallest_directory_to_delete(
        inputs,
        free_space=total_disk_space - inputs.size,
        required_space=required_space,
        sizes=[],
    )
    print(min(k))
