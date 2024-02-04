from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp = [0] * LEN

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, LEN):
            i_2 = dp[i - 2]
            i_3 = dp[i - 3]
            max_prev = max(i_2, i_3)
            dp[i] = max_prev + nums[i]

        return max(dp[LEN - 1], dp[LEN - 2])


sol = Solution()
print(sol.rob([1, 2, 7, 2, 1, 9]))
