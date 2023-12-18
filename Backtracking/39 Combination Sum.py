from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(path: List[int], tar: int, minn: int):
            if tar == 0:
                return [path]

            res = []
            for n in candidates:
                if n > tar or n < minn:
                    continue

                r = backtrack(path + [n], tar - n, n)
                res.extend(r)

            return res
 
        return backtrack([], target, 0)


sol = Solution()
print(sol.combinationSum([2, 6, 7], 8))