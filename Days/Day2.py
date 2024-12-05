file_path = "../Inputs/Day2"
def checkGradient(one, two):
    if one > two:
        return False
    elif one < two:
        return True
    else:
        return None

def checkTwoLevels(one, two):
    diff = one - two
    value = abs(diff)
    if not (value >= 1 and value <= 3):
        return False
    return True

def checkReport(report):
    levels = [int(s) for s in report.split() if s.isdigit()]
    gradient = None
    for i in range(len(levels) -1):
        if i == 0:
            gradient = checkGradient(levels[i], levels[i+1])
            if gradient is None:
                return 0
        if gradient == checkGradient(levels[i], levels[i+1]):
            if not checkTwoLevels(levels[i], levels[i+1]):
                return 0
        else:
            return 0
    return 1

def checkreport2(report):
    levels = [int(s) for s in report.split() if s.isdigit()]
    for i in range(len(levels) +1):
        if not i:
            if checkReport(report):
                return 1
            continue
        altered_report = [levels[idx] for idx in range(len(levels)) if idx != i-1]
        altered_report = ''.join(f"{x} " for x in altered_report)
        if checkReport(altered_report):
            return 1
    return 0



def checkReport2(report):
    levels = [int(s) for s in report.split() if s.isdigit()]
    gradient = None
    unsafeLevelAlready = False
    for i in range(len(levels) -1):
        if i == 0:
            if levels[i] > levels[i+1]:
                gradient = False
            elif levels[i] < levels[i+1]:
                gradient = True
            else:
                return 0
        if gradient == checkGradient(levels[i], levels[i+1]):
            safe = checkTwoLevels(levels[i], levels[i+1])
            if not safe:
                if unsafeLevelAlready:
                    return 0
                else:
                    unsafeLevelAlready = True
                    try:
                        safe = checkTwoLevels(levels[i], levels[i+2])
                        if safe:
                            continue
                        else:
                            return 0
                    except IndexError:
                        return 1
        else:
            if unsafeLevelAlready:
                return 0
            else:
                unsafeLevelAlready = True
                try:
                    if gradient == checkGradient(levels[i], levels[i + 2]):
                        safe = checkTwoLevels(levels[i], levels[i + 2])
                        if safe:
                            continue
                        else:
                            return 0
                    else:
                        return 0
                except:
                    return 1
    return 1

def part1():
    sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Process each line
            sum += checkReport(line)
        print(sum)

def part2():
    sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            sum += checkreport2(line)
            print(sum)
part2()