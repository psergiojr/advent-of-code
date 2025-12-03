import unittest


def parse_input(filename: str) -> list[tuple[str, int]]:
    data = []

    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    
    rotations = [
        ( line[0], int(line[1:]) )
        for line in data
    ]
    return rotations


def part1(filename: str) -> int:
    return count_zeroes(filename)


def part2(filename: str) -> int:
    return count_zeroes(filename, in_between=True)


def count_zeroes(filename: str, in_between: bool = False):
    dial: int = 50
    zeroes_at_end: int = 0
    zeroes_in_between: int = 0

    rotations = parse_input(filename)

    for (direction, value) in rotations:
        zeroes_in_between += value // 100 # full spins
        remainder = value % 100

        if direction == 'L':
            if dial != 0 and dial - remainder < 0:
                zeroes_in_between += 1
            dial = (dial - remainder) % 100
        elif direction == 'R':
            if dial + remainder > 100:
                zeroes_in_between += 1
            dial = (dial + remainder) % 100

        if dial == 0:
            zeroes_at_end += 1
    
    if in_between:
        return zeroes_at_end + zeroes_in_between
    else:
        return zeroes_at_end


class TestDay01(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(part1("example.txt"), 3)
    
    def test_part1_input(self):
        self.assertEqual(part1("input.txt"), 964)
    
    def test_part2_example(self):
        self.assertEqual(part2("example.txt"), 6)
    
    def test_part2_input(self):
        self.assertEqual(part2("input.txt"), 5872)


if __name__ == "__main__":
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))

    unittest.main()
