def loadItems(inputfile):
    inputdata = ''
    with open(inputfile, 'r') as f:
        inputdata = [l.rstrip() for l in f]

    return inputdata


def part1(input):
    items = loadItems(input)
    score = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3
    }
    counter = 0
    for item in items:
        counter += score[item]
    
    return counter


def part2(input):
    items = loadItems(input)
    score = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6
    }
    counter = 0
    for item in items:
        counter += score[item]
    
    return counter


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert part1("example.txt") == 15

    print(f'Part 2: {part2("input.txt")}')
    assert part2("example.txt") == 12
