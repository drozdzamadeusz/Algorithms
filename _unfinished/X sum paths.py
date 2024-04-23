from typing import List


def sumPaths(target: int, nums: List[int]):

    memo = {}

    def backtrack(target: int, curr_path: List[int]):
        if target < 0:
            return

        if target == 0:
            return [[]]

        if target in memo:
            return memo[target]


        results = []
        cache = []
        for n in nums:
            remainder = target - n
            res = backtrack(remainder, curr_path + [n])

            if res is not None:
                for p in res:
                    results.append(curr_path + [n] + p)
                    cache.append([n] + p)

        memo[target] = cache
        


    return backtrack(target, [])


print(sumPaths(5, [1, 2, 4]))
