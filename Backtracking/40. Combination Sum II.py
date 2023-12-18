from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(path: List[int], tar: int, minN: int, vis: List[bool]) -> List[List[int]]:
            if tar == 0:
                return [path]

            if minN > tar:
                return []

            res, checked = [], []
            for i, n in enumerate(candidates):
                if n > tar or n < minN or n in checked or vis[i]:
                    continue

                vis[i] = True

                r = backtrack(path + [n], tar - n, n, vis)
                res.extend(r)

                vis[i] = False
                checked.append(n)

            return res

        visited = [False for _ in range(len(candidates))]
        return backtrack([], target, 0, visited)


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
