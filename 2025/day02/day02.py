from math import ceil
from textwrap import dedent


class IdRange:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def parse_data(filename: str) -> list[IdRange]:
    data = None
    with open(filename) as f:
        data = f.read().split(',')

    ranges = []

    for pair in data:
        start, end = pair.split('-')
        ranges.append(IdRange(int(start), int(end)))

    return ranges


def part1(filename: str) -> int:
    ranges = parse_data(filename)
    invalid_ids: list[int] = []

    for ran in ranges:
        for num in range(ran.start, ran.end + 1):
            strNum = str(num)
            length = len(strNum)

            # check invalid by comparing halves
            if length % 2 == 0 and strNum[:length//2] == strNum[length//2:]:
                invalid_ids.append(num)

    return sum(invalid_ids)


def part2(filename: str) -> int:
    ranges = parse_data(filename)
    invalid_ids: list[int] = []

    for ran in ranges:
        for num in range(ran.start, ran.end + 1):
            if num < 10:
                continue
            # check invalid by rotating/wrapping characters
            rotations = set()
            strNum = str(num)
            rotations.add(strNum)
            length = len(strNum)

            for i in range(ceil(length / 2)):
                strNum = strNum[1:] + strNum[:1]
                if strNum in rotations:
                    # repeated pattern found
                    invalid_ids.append(num)
                    break
                rotations.add(strNum)
            
    return sum(invalid_ids)


if __name__ == "__main__":
    example1 = part1("example.txt")
    input1   = part1("input.txt")
    example2 = part2("example.txt")
    input2   = part2("input.txt")

    print(dedent(f"""\
    Part 1:
        Example = {example1}
        Input   = {input1}
    """))
    assert example1 == 1227775554
    assert input1 == 18952700150

    print(dedent(f"""\
    Part 2:
        Example = {example2}
        Input   = {input2}
    """))
    assert example2 == 4174379265
    assert input2 == 28858486244
