def check_position(position, matrix, char):
    (y, x) = position
    size = len(matrix)
    return (x in range(0, size) and y in range(0, size)) and matrix[y][x] == char

def check_position2(position, matrix, options):
    (y, x) = position
    size = len(matrix)
    return (x in range(0, size) and y in range(0, size)) and matrix[y][x] in options

def day4_part1(matrix):
    count = 0
    position_x = []
    for y, line in enumerate(matrix):
        position_x.extend([(x, y) for x, char in enumerate(line) if char == "X"])
    for (x, y) in position_x:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if check_position((y + i, x + j), matrix, "M"):
                    if check_position((y + 2 * i, x + 2 * j), matrix, "A"):
                        if check_position((y + 3 * i, x + 3 * j), matrix, "S"):
                            count += 1
    print(count)


def day4_part2(matrix):
    count = 0
    position_a = []
    for y, line in enumerate(matrix):
        position_a.extend(
            [(x, y) for x, char in enumerate(line)
             if char == "A" and (x in range(1, len(matrix) - 1) and y in range(1, len(matrix) - 1))])
    coordinates = [((-1,-1),(1,1)),((-1,1),(1,-1))]
    for a in position_a:
        (y,x) = a
        options = ["M","S"]
        both_diagonals = False
        for coordinate in coordinates:
            found = []
            for position in coordinate:
                (i, j) = position
                for option in options:
                    if check_position((y +i, x + j), matrix, option):
                        found.append(option)
                if ("M" in found and "S" in found):
                    both_diagonals = True
                else:
                    both_diagonals = False
        if both_diagonals:
            count += 1
    print(count)

matrix = []
file_path = "../Inputs/Day4"
with open(file_path, 'r') as file:
    for line in file:
        matrix.append(list(line.strip()))
day4_part2(matrix)
