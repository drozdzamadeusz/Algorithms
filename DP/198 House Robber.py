from typing import List
from _utils import equal


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         LEN = len(nums)

#         if LEN == 2:
#             return max(nums[0], nums[1])
#         elif LEN == 1:
#             return nums[0]

#         dp = [0] * LEN

#         dp[0] = nums[0]
#         dp[1] = nums[1]
#         dp[2] = nums[2] + nums[0]

#         for i in range(3, LEN):
#             i_3 = dp[i - 3]
#             i_2 = dp[i - 2]
#             # i - 1 is skiped
#             dp[i] = max(i_3, i_2) + nums[i]

#         return max(dp[LEN - 1], dp[LEN - 2])

class Solution:
    def rob(self, nums: List[int]) -> int:
        LEN = len(nums)

        if LEN == 2:
            return max(nums[0], nums[1])
        elif LEN == 1:
            return nums[0]

        fst = nums[0]
        sec = nums[1]
        # House that have to be skipped in next iteration
        prev = nums[2] + fst

        # [fst, sec, prev, i, i + 1]
        for i in range(3, LEN):
            if (fst > sec):
                res = fst + nums[i]
                sec = prev
            else:
                res = sec + nums[i]
                fst = prev
            prev = res
            
        return max(fst, sec, prev)


sol = Solution()
equal(sol.rob([1, 2, 3, 1]))
equal(sol.rob([2, 7, 9, 3, 1]), 12)
