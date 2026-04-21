def is_safe(entryRow):
    if entryRow[1] > entryRow[0]:
        increment = 1

    elif entryRow[1] < entryRow[0]:
        increment = -1

    else:
        return False

    for i in range(len(entryRow) - 1):
        diff = entryRow[i + 1] - entryRow[i]

        if increment == 1 and diff <= 0:
            return False
        
        if increment == -1 and diff >= 0:
            return False
        
        if abs(diff) > 3:
            return False

    return True

def main():
    answer = 0

    with open("input.txt", "r") as file:
        for line in file:
            intEntries = [int(n) for n in line.split()]

            if is_safe(intEntries):
                answer += 1

    print(answer)

main()