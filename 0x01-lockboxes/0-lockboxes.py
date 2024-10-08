#!/usr/bin/python3
"""define method canUnlockAll that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened.

    Args:
        boxes (list of lists): n number of locked boxes,
            Each box is numbered sequentially from 0 to n - 1,
            each box may contain keys to the other boxes.

    Returns:
        boolean: True if all boxes can be opened, else return False
    """
    keys_set = set()
    keys_set.add(0)
    answer = set(list(range(len(boxes))))

    if boxes[0] == [] and len(boxes) > 1:
        return False

    if len(boxes) == 1:
        return True

    def unlock_all(boxes, box_index):
        """helper function to unlock all boxes passed from canUnlockAll

        Args:
            boxes (list of lists): locked boxes
            box_index (+ve integer): the index of the box that will be opened
                                    (key of the list)
        """
        for key in boxes[box_index]:
            if (key not in keys_set) and (not key >= len(boxes)):
                keys_set.add(key)
                unlock_all(boxes, key)

    unlock_all(boxes, 0)

    return answer == keys_set


# boxes = [[1], [2], [3], [4], []]
# boxes = [[1], [2], [3], [4], [5], []]
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# boxes = [[1], [2], [3, 5], [4], [7], []]
# boxes = [[1], [2], [], [4]]
# boxes = [[1], [2], [100], []]
# boxes = [[], [0, 1, 2], [1, 22, 3], []]
# boxes = [[1], [3], [2], []]  # Should return False
# boxes = [[]]  # Should return True
# boxes = [[]]  # Should return True
# boxes = [[1], []]  # Should return True
# boxes = [[], [0]]  # Should return True
# boxes = [[1, 2], [3], [], [4], []]
# boxes = [[0], []]  # Should return False
# boxes = [[1, 1, 1], [2], [3], []]  # Should return True
# boxes = [[], [1], [2], []]  # Returns False
# print(canUnlockAll(boxes))

"""

print(canUnlockAll(boxes))
 """
