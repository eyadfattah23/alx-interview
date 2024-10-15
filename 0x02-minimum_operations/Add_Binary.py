#!/usr/bin/python3
def addBinary(a: str, b: str) -> str:

    i, j = len(a) - 1, len(b) - 1
    result = []
    cache = '0'

    while i >= 0 and j >= 0:

        if a[i] == '1' and b[j] == '1':
            result.append(max('0', cache))
            cache = '1'

        elif ((a[i] == '1' and b[j] == '0') or (a[i] == '0' and b[j] == '1')):
            if cache == '0':
                result.append(max('1', cache))
            else:
                result.append('0')
                cache = '1'

        else:
            if cache == '0':
                result.append('0')
            else:
                result.append('1')
                cache = '0'

        i -= 1
        j -= 1

    while i >= 0:
        if cache == '1' and a[i] == '1':
            result.append('0')

        elif cache == '1' and a[i] == '0':
            result.append('1')
            cache = '0'
        else:
            result.append(a[i])

        i -= 1

    while j >= 0:
        if cache == '1' and b[j] == '1':
            result.append('0')

        elif cache == '1' and b[j] == '0':
            result.append('1')
            cache = '0'
        else:
            result.append(b[j])

        j -= 1

    if cache == '1':
        result.append(cache)

    result.reverse()
    return ''.join(result)


a = "1010"
b = "1011"
print(addBinary(a, b))

a = "11"
b = "1"
print(addBinary(a, b))
