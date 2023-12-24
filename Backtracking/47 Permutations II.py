from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path: List[int], vis: List[False]):

            if len(path) == len(nums):
                return [path]

            res = []
            picked = set()

            for i, n in enumerate(nums):
                if n in picked or vis[i]:
                    continue

                vis[i] = True

                res.extend(backtrack(path + [n], vis))

                vis[i] = False

                picked.add(n)

            return res

        visited = [False for _ in nums]
        return backtrack([], visited)


sol = Solution()
print(sol.permuteUnique([1, 1, 2]))
