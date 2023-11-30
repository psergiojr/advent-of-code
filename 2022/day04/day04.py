def loadItems(file):
    lines = []
    items = []
    with open(file, 'r') as f:
        lines = [l.rstrip() for l in f]

    for line in lines:
        a, b = line.split(',')
        range_a = [int(x) for x in a.split('-')]
        range_b = [int(x) for x in b.split('-')]
        elf_a = set(range( range_a[0], range_a[-1]+1 ))
        elf_b = set(range( range_b[0], range_b[-1]+1 ))
        items.append((elf_a, elf_b))

    return items


def part1(file):
    result = 0
    items = loadItems(file)

    for elf_a, elf_b in items:
        if elf_a.issubset(elf_b) or elf_b.issubset(elf_a):
            result += 1

    return result


def part2(file):
    result = 0
    items = loadItems(file)

    for elf_a, elf_b in items:
        if elf_a & elf_b:
            result += 1

    return result


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert part1("example.txt") == 2

    print(f'Part 2: {part2("input.txt")}')
    assert part2("example.txt") == 4
