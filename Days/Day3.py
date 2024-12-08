import re

def day3_part1(input):
    pattern = "mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    sum = 0
    for match in matches:
        sum += int(match[0]) * int(match[1])
    print(sum)

def day3_part2(input):
    pattern = "mul\((\d+,\d+)\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, input)
    summe = 0
    condition = 1
    for match in matches:
        match = [x for x in match if x][0]
        if match == "do()":
            condition = 1
        elif match == "don't()":
            condition = 0
        else:
            if condition:
                split = [int(x) for x in match.split(",")]
                summe += split[0] * split[1]
    print(summe)

file_path = "../Inputs/Day3"
with open(file_path, 'r') as file:
    input = file.read()
    day3_part2(input)