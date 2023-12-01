def load_data(file_path: str):
    data = []
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data

def part1(file_path: str):
    lines = load_data(file_path)
    calibration_values = []

    for line in lines:
        first_digit: int = None
        last_digit: int = None
        for letter in line:
            if letter.isdigit():
                if not first_digit: first_digit = letter
                last_digit = letter
        calibration_values.append(int(first_digit + last_digit))

    return sum(calibration_values)

def part2(file_path: str):
    lines = load_data(file_path)
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
    calibration_values = []

    for line in lines:
        first_digit: int = None
        last_digit: int = None
        number_buffer: str = '     '
        for letter in line:
            if letter.isdigit():
                if not first_digit: first_digit = letter
                last_digit = letter
                # reset number buffer
                number_buffer = '     '
            else:
                number_buffer = number_buffer[1:] + letter
                # print(number_buffer)
                num = None

                if number_buffer[-3:] in numbers:
                    num = numbers[number_buffer[-3:]]
                elif number_buffer[-4:] in numbers:
                    num = numbers[number_buffer[-4:]]
                elif number_buffer in numbers:
                    num = numbers[number_buffer]
                
                # print(f'Number found: {num}')
                if num:
                    if not first_digit: first_digit = num
                    last_digit = num
        
        calibration_values.append(int(first_digit + last_digit))
    # print(calibration_values)
    return sum(calibration_values)


if __name__ == '__main__':
    print(f'Part 1: {part1("input.txt")}')
    assert(part1('example1.txt') == 142)

    print(f'Part 2: {part2("input.txt")}')
    assert(part2('example2.txt') == 281)
