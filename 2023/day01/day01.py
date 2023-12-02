numbers = {
    'one'  : '1',
    'two'  : '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six'  : '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9',
}

def parse_calibration_values(file_path: str, check_text: bool = False) -> int:
    calibration_values = []
    
    with open(file_path, 'r') as f:
        for line in f:
            digits = []
            buffer = '     '
            for char in line:
                if char.isdigit():
                    digits.append(char)
                    # resetting the buffer
                    buffer = '     '
                    
                elif check_text:
                    buffer = buffer[1:] + char
                    for i in (3, 4, 5):
                        if buffer[-i:] in numbers:
                            digits.append(numbers[buffer[-i:]])
                            break

            calibration_values.append(int(digits[0] + digits[-1]))
    
    return sum(calibration_values)


def part1(file_path: str) -> int:
    return parse_calibration_values(file_path)


def part2(file_path: str) -> int:
    return parse_calibration_values(file_path, check_text=True)


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert part1('example1.txt') == 142

    print(f'Part 2: {part2("input.txt")}')
    assert part2('example2.txt') == 281
