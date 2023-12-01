def load_data(file_path: str):
    data = []
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data

def part1(lines):
    calibration_values = []
    for line in lines:
        first_digit: int = None
        last_digit: int = None
        for letter in line:
            if letter.isdigit():
                if not first_digit:
                    first_digit = letter
                last_digit = letter
        calibration_values.append(int(first_digit + last_digit))
    # print(calibration_values)
    return sum(calibration_values)

def part2():
    pass

if __name__ == '__main__':
    example_part1 = part1(load_data('example.txt'))
    assert(example_part1 == 142)
    input_part1 = part1(load_data('input.txt'))
    print(f'Part 1: {input_part1}')
