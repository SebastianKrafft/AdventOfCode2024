from collections import Counter
file_path = "../Inputs/Day1"
left = []
right = []
with open(file_path, 'r') as file:
    for line in file:
        # Process each line
        numbers = [int(s) for s in line.split() if s.isdigit()]
        left.append(numbers[0])
        right.append(numbers[1])

def part1(left, right):
    left = sorted(left)
    right = sorted(right)
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    print(sum)

def part2(left, right):
    left = set(left)
    right = Counter(right)
    sum = 0
    for number in left:
        sum += number * right[number]
    print(sum)
part2(left, right)