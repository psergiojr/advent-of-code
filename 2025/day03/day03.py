from textwrap import dedent
import unittest


def highest_joltage(line: str, digits: int) -> int:
    index_start: int = 0
    index_end: int = len(line) - digits + 1
    joltage = []

    for i in range(digits):
        highest = max(line[index_start:index_end])
        highest_index = line.index(highest, index_start, index_end)
        joltage.append(highest)
        index_start = highest_index + 1
        index_end += 1

    return int(''.join(joltage))


def part1(filename: str) -> int:
    joltages = []

    with open(filename) as f:
        joltages = [
            highest_joltage(line.strip(), 2)
            for line in f.readlines()
        ]

    return sum(joltages)


def part2(filename: str) -> int:
    joltages = []

    with open(filename) as f:
        joltages = [
            highest_joltage(line.strip(), 12)
            for line in f.readlines()
        ]
    
    return sum(joltages)


if __name__ == '__main__':
    example1 = part1("example.txt")
    input1 = part1("input.txt")
    example2 = part2("example.txt")
    input2 = part2("input.txt")

    print(dedent(f"""\
        Part 1:
            example: {example1}
            input:   {input1}

        Part 2:
            example: {example2}
            input:   {input2}
    """))

    # Using TestCase unittests here because the stack trace error messages are
    # better when TDDing than just plain asserts

    class TestDay3(unittest.TestCase):
        def test_joltage_part1(self):
            self.assertEqual( highest_joltage('987654321111111', 2), 98 )
            self.assertEqual( highest_joltage('811111111111119', 2), 89 )
            self.assertEqual( highest_joltage('234234234234278', 2), 78 )
            self.assertEqual( highest_joltage('818181911112111', 2), 92 )

        def test_part1_example(self):
            self.assertEqual(example1, 357)

        def test_part1_input(self):
            self.assertEqual(input1, 17330)

        def test_part2_example(self):
            self.assertEqual(example2, 3121910778619)

        def test_part2_input(self):
            self.assertEqual(input2, 171518260283767)

        def test_joltage_part2(self):
            self.assertEqual( highest_joltage('987654321111111', 12), 987654321111 )
            self.assertEqual( highest_joltage('811111111111119', 12), 811111111119 )
            self.assertEqual( highest_joltage('234234234234278', 12), 434234234278 )
            self.assertEqual( highest_joltage('818181911112111', 12), 888911112111 )

    unittest.main()
