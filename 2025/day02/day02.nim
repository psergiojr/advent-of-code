import std/[strformat, strutils, math, sets]


type IdRange = object
    first: int
    last: int


proc parse_data(filename: string): seq[IdRange] =
    let data: seq[string] = filename.readFile.split(',')

    for idrange in data:
        result.add IdRange(
            first: idrange.split('-')[0].parseInt,
            last: idrange.split('-')[1].parseInt, )


proc part1(filename: string): int =
    let ranges: seq[IdRange] = parse_data(filename)

    for ran in ranges:
        for num in ran.first..ran.last:
            var
                strNum: string = intToStr(num)
                length: int = strNum.len
            
            if length mod 2 == 0:
                var
                    half1: string = strNum[0..<(length div 2)]
                    half2: string = strNum[(length div 2)..strNum.high]

                if half1 == half2:
                    result += num


proc part2(filename: string): int =
    let ranges: seq[IdRange] = parse_data(filename)
    
    for ran in ranges:
        for num in ran.first..ran.last:
            if num < 10:
                continue
            # cycle / wrap around to find repeated patterns
            var
                rotations: HashSet[string] = initHashSet[string]()
                strNum: string = intToStr(num)
                length: int = strNum.len
            
            rotations.incl strNum

            for i in 1..ceil(length / 2).toInt:
                strNum = strNum[1..strNum.high] & strNum[0]
                if strNum in rotations:
                    # pattern found
                    result += num
                    break
                rotations.incl strNum


when isMainModule:
    let
        example1 = part1("example.txt")
        input1   = part1("input.txt")
        example2 = part2("example.txt")
        input2   = part2("input.txt")

    echo dedent(&"""
    Part 1:
        Example = {example1}
        Input   = {input1}
    """)
    doAssert example1 == 1227775554
    doAssert input1 == 18952700150

    echo dedent(&"""
    Part 2:
        Example = {example2}
        Input   = {input2}
    """)
    doAssert example2 == 4174379265
    doAssert input2 == 28858486244
