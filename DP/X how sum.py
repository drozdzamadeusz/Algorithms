from typing import List


def howSum(target: int, nums: List[int], memo: dict):
    if target in memo:
        return memo[target]

    if target < 0:
        return None

    if target == 0:
        return []

    for n in nums:
        remainder = target - n
        remainderRes = howSum(remainder, nums, memo)
        if (remainderRes is not None):
            memo[target] = remainderRes + [n]
            return memo[target]

    memo[target] = None
    return None


print(howSum(7, [3, 2, 2, 7], {}))
