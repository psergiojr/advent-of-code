def load_data(file: str) -> dict:
    data = ''
    with open(file) as f:
        data = [l.rstrip() for l in f.read().split('$ ')]

    tree = build_dir_tree(data)
    size_dict = {}
    calc_node_size(tree, name='/', size_dict=size_dict)

    return size_dict


def build_dir_tree(input_data: list[str]) -> dict:
    """Tree of dicts.

    - dirs -> dicts,
    - files -> ints
    """
    root = {}
    cursor = [ root ] # keep track of the "path" so we can go back

    for line in input_data:
        if line.startswith('cd'):
            path = line.split()[-1]
            if path == '/':
                cursor = [root]
            elif path == '..':
                cursor.pop()
            else:
                cursor.append(cursor[-1][path])

        elif line.startswith('ls'):
            ls = line.splitlines()[1:]
            for item in ls:
                if item.startswith('dir'):
                    dirname = item.split()[-1]
                    cursor[-1][dirname] = dict()
                else:
                    size, filename = item.split()
                    cursor[-1][filename] = size

    return root


def calc_node_size(node, name, size_dict) -> int:
    size = 0
    if type(node) is str:
        size = int(node)
    elif type(node) is dict:
        for n in node:
            full_name = " ".join([name, n])
            child_size = calc_node_size(node[n], full_name, size_dict)
            size += child_size
        size_dict[name] = size

    return size


def part1(file: str) -> int:
    sizes = load_data(file)
    result = sum([sizes[d] for d in sizes if sizes[d] <= 100000])

    return result


def part2(file: str) -> int:
    sizes = load_data(file)
    result = 0

    total_disk_space = 70000000
    min_needed_space = 30000000
    free_space = total_disk_space - sizes['/']
    min_to_clean = min_needed_space - free_space

    result = min([sizes[d] for d in sizes if sizes[d] >= min_to_clean])

    return result


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert part1('example.txt') == 95437

    print(f'Part 2: {part2("input.txt")}')
    assert part2('example.txt') == 24933642
