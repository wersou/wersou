#3 * x + 9 * y + 8 * z == 79
def findXYZ(n):
    solutions = []

    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                if (3 * x + 9 * y + 8 * z == 79):
                    solutions.append(x)
                    solutions.append(y)
                    solutions.append(z)
                    solutions.append(',')

    return solutions


print(findXYZ(10))


