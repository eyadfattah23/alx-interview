#!/usr/bin/python3
def canUnlockAll(boxes):
    keys_set = set()
    keys_set.add(0)

    answer = set(list(range(len(boxes))))

    if boxes[0] == []:
        return False

    def unlockAll(boxes, box_idx):

        if box_idx not in keys_set or box_idx == 0:
            keys_set.add(box_idx)

            for key in boxes[box_idx]:
                unlockAll(boxes, key)

    unlockAll(boxes, 0)
    if keys_set == answer:
        return True
    return False


# print(canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))


""" def unlockAll(boxes, keys_set_set):
sets = {1, 2, 3, 4, 5, 6}
# keys_set.update([key for key in boxes[0]])
        for box_idx in range(len(boxes)):
            for key in boxes[box_idx]:
                if key in keys_set_set:
                    continue
                else:
                    new_boxes = boxes.copy()
                    new_boxes.pop(box_idx)
                    unlockAll(new_boxes, keys_set_set)
                    keys_set.add(key)
    return unlockAll(boxes, keys_set) """
