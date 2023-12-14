from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(path: List[int], used: Set[int], res: List[List[int]]):

            if len(path) == len(nums):
                res.append(path.copy())
                return

            for n in nums:
                if not n in used:

                    used.add(n)
                    path.append(n)

                    backtrack(path, used, res)

                    used.remove(n)
                    path.pop()

            return res

        return backtrack([], set(), [])


sol = Solution().permute([1, 2])
print(sol)
