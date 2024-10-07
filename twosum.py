#!/usr/bin/python3

def twoSum(nums, target):
    hashmap = dict()
    ans = []

    for i in range(len(nums)):

        num = target - nums[i]
        if hashmap.get(num) is not None:
            ans.append(i)
            ans.append(hashmap[target - nums[i]])
        else:
            hashmap[nums[i]] = i

    return ans


print(twoSum([3, 3], 6))
