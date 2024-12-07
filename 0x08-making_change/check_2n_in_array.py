# solution to leet 1346
def checkIfExist(arr):
    seen = dict()

    for i in range(len(arr)):
        if arr[i] * 2 in seen:
            return True
        seen[arr[i]] = i
    for i in range(len(arr)):
        if arr[i] * 2 in seen and i != seen.get(arr[i]*2):
            return True

    return False


arr = [-2, 0, 10, -19, 4, 6, -8]  # f
print(checkIfExist(arr))

arr = [7, 1, 14, 11]  # t
print(checkIfExist(arr))

arr = [3, 1, 7, 11]  # f
print(checkIfExist(arr))

arr = [10, 2, 5, 3]  # t
print(checkIfExist(arr))
