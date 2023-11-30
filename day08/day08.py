def loadItems(file):
    data = ''
    with open(file) as f:
        data = [l.rstrip() for l in f]
    return data


def part1(file):
    items = loadItems(file)
    result = 0
    visible_coords = set()

    for x, row in enumerate(items, start=1):
        for col in visible_trees(row):
            visible_coords.add((x, col))
    
    for y, col in enumerate(zip(*items), start=1):
        for row in visible_trees(col):
            visible_coords.add((row, y))

    result = len(visible_coords)
    return result


def visible_trees(line):
    forwards = enumerate(line, start=1)
    backwards = reversed(list(enumerate(line, start=1)))
    visible = set()

    for line_of_sight in (forwards, backwards):
        tallest = -1
        for tree, height in line_of_sight:
            if int(height) > tallest:
                visible.add(tree)
                tallest = int(height)
    return visible


def scenic_score(row, col):
    score = 0

    return score


if __name__ == '__main__':
    assert part1("example.txt") == 21
    print(f'Part 1: {part1("input.txt")}')

    assert scenic_score(2, 3) == 4
    assert scenic_score(4, 3) == 8