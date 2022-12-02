def loadItems(inputfile):
    inputdata = ''
    with open(inputfile, 'r') as f:
        inputdata = f.read()
    
    return [
        list(map(int, x.splitlines())) 
        for x 
        in inputdata.split('\n\n')
    ]


def part1(input):
    """Max calories of all elves"""
    elves = loadItems(input)
    maxcalories = max([sum(x) for x in elves])

    return maxcalories


def part2(input):
    """Sum of calories from the top 3 elves"""
    elves = loadItems(input)
    calories = [sum(x) for x in elves]
    calories.sort()
    top3 = calories[-3:]

    return sum(top3)


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert part1("example.txt") == 24000

    print(f'Part 2: {part2("input.txt")}')
    assert part2("example.txt") == 45000
