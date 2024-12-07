def addSpaces(s: str, spaces):

    result = []

    for j in range(1, len(spaces)):
        result.append(s[spaces[j-1]:spaces[j]])
    result.append(s[spaces[-1]:])
    return " ".join(result)

    while j < len(spaces):
        s = s[:spaces[j] + j] + ' ' + s[spaces[j] + j:]
        j += 1
    return s


print(addSpaces("icodeinpython", [1, 5, 7, 9]))
