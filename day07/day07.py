def load_data(file):
    data = ''
    with open(file) as f:
        data = [l.rstrip() for l in f.read().split('$ ')]
    # print(data)
    return data


def build_dir_tree(input_data: list[str]):
    root = {}
    # dir -> dict
    # file -> int
    cursor = [ root ] # maintain the "path" so we can go "back" 

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


def calc_node_size(node, name, size_dict):
    size = 0
    if type(node) is str:
        size = int(node)
    elif type(node) is dict:
        for n in node:
            child_size = calc_node_size(node[n], n, size_dict)
            size += child_size
        size_dict[name] = size

    return size


def part1(file):
    tree = build_dir_tree(load_data(file))
    size_dict = {}
    # print(tree)
    calc_node_size(tree, name='/', size_dict=size_dict)
    # print(size_dict)

    result = 0
    for dir_node in size_dict:
        if size_dict[dir_node] <= 100000:
            result += size_dict[dir_node]

    return result


def part2():
    pass


if __name__ == '__main__':
    print(f'Part 1: {part1("example.txt")}')
    assert part1('example.txt') == 95437
