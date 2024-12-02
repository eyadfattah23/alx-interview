#!/usr/bin/python3
"""solution to jump game problem leet 55"""


def canJump(nums):

    i = 0
    while i < len(nums):
        jumps = nums[i]

        if i + jumps >= len(nums) - 1:
            return True

        if nums[i] == 0:
            return False

        new_jumps = -1
        new_idx = 0
        for j in range(i+1, jumps + i + 1):
            if nums[j] + j >= len(nums) - 1:
                return True
            if nums[j] >= new_jumps:
                if nums[j] != 0 and max(nums[j+1:j+1+nums[j]]) != 0:
                    new_jumps = nums[j]
                    if new_jumps + j >= len(nums) - 1:
                        return True
                    new_idx = j

        if new_jumps <= 0:
            return False

        i = new_idx


nums = [2, 5, 0, 0]  # true
print(canJump(nums))

nums = [4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]  # true
print(canJump(nums))

nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(canJump(nums))  # true

nums = [3, 2, 1, 0, 4]
print(canJump(nums))  # false


nums = [1, 2, 0, 1]
print(canJump(nums))  # true

nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # true
