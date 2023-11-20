from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for n in numsSet:
            if n - 1 not in numsSet:
                seqLen = 1
                nextNum = n + 1
                while nextNum in numsSet:
                    seqLen += 1
                    nextNum += 1
                res = max(seqLen, res)

        return res


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
