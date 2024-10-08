#!/usr/bin/python3
def canUnlockAll(boxes):
    keys_set = set()
    keys_set.add(0)
    answer = set(list(range(len(boxes))))

    if boxes[0] == []:
        return False

    def unlock_all(boxes, box_index):
        for key in boxes[box_index]:
            if (not key in keys_set) and (not key >= len(boxes)):
                keys_set.add(key)
                unlock_all(boxes, key)

    unlock_all(boxes, 0)

    if answer == keys_set:
        return True
    return False


# print(canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]))

boxes = [[1], [2], [3, 5], [4], [7], []]
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
