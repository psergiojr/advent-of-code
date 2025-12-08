import std/[strutils, math]


type
    Direction = enum
        Left = "L"
        Right = "R"

    Rotation = object
        direction: Direction
        value: int


proc parse_data(filename: string): seq[Rotation] =
    for line in filename.readFile.splitLines:
        result.add Rotation(
            direction: parseEnum[Direction]($line[0]),
            value: parseInt(line[1..line.high])
        )


proc count_zeroes(filename: string, count_between: bool = false): int =
    let rotations: seq[Rotation] = parse_data(filename)
    var
        dial: int = 50
        remainder: int
        in_between: int
    
    for rotation in rotations:
        in_between += rotation.value.euclDiv 100
        remainder = rotation.value.euclMod 100

        case rotation.direction
        of Left:
            if dial != 0 and dial - remainder < 0:
                inc in_between
            dial = (dial - remainder).euclMod 100
        of Right:
            if dial + remainder > 100:
                inc in_between
            dial = (dial + remainder).euclMod 100
        
        if dial == 0:
            inc result
    
    if count_between:
        result += in_between


proc part1(filename: string): int =
    result = count_zeroes(filename)
    echo "Part 1 (", filename, "): ", result


proc part2(filename: string): int =
    result = count_zeroes(filename, count_between = true)
    echo "Part 2 (", filename, "): ", result


when isMainModule:
    doAssert part1("example.txt") == 3
    doAssert part1("input.txt") == 964

    doAssert part2("example.txt") == 6
    doAssert part2("input.txt") == 5872
