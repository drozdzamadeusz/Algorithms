import math
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path: List[int], vis: List[bool], minN: int):
            res = [path]

            if len(path) == len(nums):
                return res

            seen = set()  # Track elements added at this level, so only distinct numbers will be checked
            for i, n in enumerate(nums):
                if n < minN or n in seen or vis[i]:
                    continue

                vis[i] = True

                r = backtrack(path + [n], vis, n)
                res.extend(r)

                vis[i] = False

                seen.add(n)

            return res

        visited = [False for _ in nums]
        return backtrack([], visited, -math.inf)

# Better sol
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

#         def backtrack(path: List[int], start: int):
#             res = [path]

#             if len(path) == len(nums):
#                 return res

#             seen = set()  # Track elements added at this level, so only distinct numbers will be checked
#             for i in range(start, len(nums)):
#                 n = nums[i]

#                 if n in seen:
#                     continue

#                 r = backtrack(path + [n], i + 1)
#                 res.extend(r)

#                 seen.add(n)

#             return res

#         return backtrack([], 0)



sol = Solution()
res = sol.subsetsWithDup([1, 2, 2])
print(res)
