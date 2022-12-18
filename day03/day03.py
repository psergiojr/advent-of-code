values = dict(
    zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 53))
)


def loadItems(filename):
    data = ''
    with open(filename, 'r') as f:
        data = [l.rstrip() for l in f]
    
    return data


def part1(file):
    items = loadItems(file)
    repeated = []

    for item in items:
        mid = len(item)//2
        half1 = set(item[:mid])
        half2 = set(item[mid:])

        # &: set intersection operator
        repeated.append( (half1 & half2).pop() )
        
    result = sum([values[l] for l in repeated])
    return result


def part2(file):
    items = loadItems(file)
    repeated = []

    while items:
        a = set(items.pop(0))
        b = set(items.pop(0))
        c = set(items.pop(0))

        # &: set intersection operator
        repeated.append( (a & b & c).pop() )

    result = sum([values[l] for l in repeated])
    return result


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert part1('example.txt') == 157

    print(f'Part 2: {part2("input.txt")}')
    assert part2('example.txt') == 70
