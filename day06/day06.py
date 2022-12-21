def loadInput(file):
    data = ''
    with open(file) as f:
        data = f.read()
    return data


def decode_signal(data: str, chars: int):
    marker: int = 0
    last_n = []
    for char in data:
        if len(set(last_n)) == chars:
            break
        if len(last_n) == chars:
            last_n.pop(0)
        marker += 1
        last_n.append(char)
    return marker


def part1(data: str):
    marker = decode_signal(data, 4)
    return marker


def part2(data: str):
    marker: int = decode_signal(data, 14)
    return marker


if __name__ == '__main__':
    examples = (
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26),
    )
    for example, p1, p2 in examples:
        assert part1(example) == p1
        assert part2(example) == p2
    
    print(f'Part 1: {part1(loadInput("day06/input.txt"))}')
    print(f'Part 2: {part2(loadInput("day06/input.txt"))}')
