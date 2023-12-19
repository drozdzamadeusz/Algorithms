import math
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path: List[int], vis: List[bool], minN: int):
            res = [path]

            if len(path) == len(nums):
                return res

            seen = set()  # Only distinct numbers will be checked
            for i, n in enumerate(nums):

                if n < minN or n in seen or vis[i]:
                    continue

                vis[i] = True
                res.extend(backtrack(path + [n], vis, n))
                vis[i] = False

                seen.add(n)

            return res

        visited = [False for _ in nums]
        return backtrack([], visited, -math.inf)


sol = Solution()
res = sol.subsetsWithDup([2, 1, 2])
print(res)


# A more elegant solution where the visited array is replaced by a start index array.
# Unfortunately, it doesn't work correctly in all cases - Works for sorted input!
#
#     Input                       Result
#   [1, 2, 2] -> [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
#   [2, 1, 2] -> [[], [1], [2], [1, 2], [2, 2]           ]
#
# This approach fails to return the last path, since the array is reduced from the start
# and the last value is at index 0. Input array would have to be sorted first.


# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

#         def backtrack(path: List[int], start: int, minN: int):
#             res = [path]

#             if len(path) == len(nums):
#                 return res

#             seen = set()  # Only distinct numbers will be checked
#             for i in range(start, len(nums)):
#                 n = nums[i]

#                 if n < minN or n in seen:
#                     continue

#                 res.extend(backtrack(path + [n], i + 1, n))

#                 seen.add(n)

#             return res

#         return backtrack([], 0, -math.inf)
