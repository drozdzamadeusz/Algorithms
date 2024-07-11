from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        longest = 0
        l, r = 0, 0

        while r < len(nums):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest


sol = Solution()
print(sol.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
