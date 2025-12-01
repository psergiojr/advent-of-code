def part1(filename: str) -> int:
    data = []
    angle: int = 50
    zero_counter: int = 0

    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    
    for spin in data:
        if spin.startswith('L'):
            angle = (angle - int(spin[1:])) % 100
        elif spin.startswith('R'):
            angle = (angle + int(spin[1:])) % 100

        if angle == 0:
            zero_counter += 1
    
    return zero_counter


if __name__ == "__main__":
    result = part1("example.txt")
    print(f"Part 1 (example): {result}")
    assert result == 3

    result = part1("input.txt")
    print(f"Part 1 (input): {result}")
