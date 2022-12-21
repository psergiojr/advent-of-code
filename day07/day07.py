def load_data(file):
    data = ''
    with open(file) as f:
        data = [l.rstrip() for l in f.read().split('$ ')]
    # print(data)
    return data


def build_dir_tree(input_data: str):
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


def calc_size(tree, size_list):
    if type(tree) == 'str':
        pass
    if type(tree) == 'list':
        pass

    return size_list


def part1(file):
    tree = build_dir_tree(load_data(file))
    print(tree)

    return tree


def part2():
    pass


if __name__ == '__main__':
    print(f'Part 1: {part1("example.txt")}')
    assert part1('example.txt') == 95437
