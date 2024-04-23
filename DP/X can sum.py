from typing import List


def canSum(target: int, nums: List[int], cache: dict):
    if target in cache:
        return cache[target]

    if target < 0:
        return False

    if target == 0:
        return True

    for n in nums:
        if (canSum(target - n, nums, cache)):
            cache[target] = True
            return True

    cache[target] = False
    return False


print(canSum(7, [5, 3, 4, 7], {}))
print(canSum(7, [2, 4, 10], {}))
