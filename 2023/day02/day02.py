import re

def calculate_cubes(file_path: str) -> (int, int):
    games_p1 = []
    games_p2 = []

    with open(file_path, 'r') as f:
        for line in f:
            game = {
                'red'   : 0,
                'green' : 0,
                'blue'  : 0,
            }
            name, rounds = line.split(': ')
            cubes = [
                x.split()
                for x 
                in re.split('; |, ', rounds.strip())
            ]
            for amount, color in cubes:
                game[color] = max(game[color], int(amount))

            if (game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14):
                games_p1.append(int(name.split()[1]))
            
            games_p2.append(game['red'] * game['green'] * game['blue'])
            
    return (
        sum(games_p1),
        sum(games_p2)
    )


if __name__ == '__main__':
    example_1, example_2 = calculate_cubes("example.txt")
    part_1, part_2 = calculate_cubes("input.txt")

    print(f'Part 1: {part_1}')
    assert example_1 == 8

    print(f'Part 2: {part_2}')
    assert example_2 == 2286
