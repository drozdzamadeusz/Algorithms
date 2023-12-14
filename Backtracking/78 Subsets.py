
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start_idx: int, path: List[int], res: List[int]):
            res.append(path)

            for i in range(start_idx, len(nums)):
                
                new_path = path + [nums[i]]
                
                backtrack(i + 1, new_path, res)

            return res
        
        return backtrack(0, [], [])


sol = Solution().subsets([1, 2, 3])
print(sol)
