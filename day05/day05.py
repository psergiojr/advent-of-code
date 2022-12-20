import re
from enum import Enum


class CraneModel(Enum):
    CRATEMOVER_9000 = 1
    CRATEMOVER_9001 = 2


def load_items(file: str):
    crates_data = ''
    moves_data = ''
    with open(file, 'r') as f:
        crates_data, moves_data = [l for l in f.read().split('\n\n')]
    
    crates = parse_crates(crates_data)
    moves = parse_moves(moves_data)
    
    return (crates, moves)


def parse_crates(layers: str):
    crates = {}
    for layer in layers.splitlines()[:-1]:
        for k,v in enumerate(layer[1::4]):
            if (k+1) not in crates.keys():
                crates[k+1] = list()
            if v == ' ':
                continue
            crates[k+1].append(v)
            
    return crates


def parse_moves(steps: str):
    move_set = []
    for step in steps.splitlines():
        instruction = re.match(r'move (\d*) from (\d*) to (\d*)', step)
        move_set.append(
            tuple(map(lambda n: int(n), instruction.groups()))
        )
    return move_set


def rearrange_crates(file, model = CraneModel.CRATEMOVER_9000):
    crates, moves = load_items(file)
    stack_tops = ''
    for step in moves:
        ammount, origin, destination = step

        if model is CraneModel.CRATEMOVER_9000:
            for i in range(ammount):
                crates[destination].insert(0, crates[origin].pop(0) )

        elif model is CraneModel.CRATEMOVER_9001:
            crates[destination] = crates[origin][0:ammount] + crates[destination]
            crates[origin] = crates[origin][ammount:]

    stack_tops = ''.join([crates[s][0] for s in crates])
    return stack_tops


def part1(file: str):
    stack_tops = rearrange_crates(file)
    return stack_tops


def part2(file: str):
    stack_tops = rearrange_crates(file, model = CraneModel.CRATEMOVER_9001)
    return stack_tops


if __name__ == '__main__':
    print(f'Part 1: {part1("day05/input.txt")}')
    assert part1("day05/example.txt") == 'CMZ'

    print(f'Part 2: {part2("day05/input.txt")}')
    assert part2("day05/example.txt") == 'MCD'
