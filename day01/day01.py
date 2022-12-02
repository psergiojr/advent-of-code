example = ''
with open('example.txt') as f:
    example = f.read()

input = ''
with open('input.txt') as f:
    input = f.read()


def part1(input):
    """Max calories of all elves"""
    elves = [
        list(map(int, x.splitlines())) 
        for x 
        in input.split('\n\n')
    ]
    
    maxcalories = max([sum(x) for x in elves])

    return maxcalories


def part2(input):
    """Sum of calores for the top 3 elves"""
    elves = [
        list(map(int, x.splitlines())) 
        for x 
        in input.split('\n\n')
    ]

    calories = [sum(x) for x in elves]
    calories.sort()
    top3 = calories[-3:]

    return sum(top3)


if __name__ == '__main__':
    print(f'Part 1: {part1(input)}')
    assert part1(example) == 24000

    print(f'Part 2: {part2(input)}')
    assert part2(example) == 45000