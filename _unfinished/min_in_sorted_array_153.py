from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:

            m = (l + r) // 2

            res = min(res, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return res


# [5, 1, 2, 3, 4]

sol = Solution()
print(sol.findMin([5, 1, 2, 3, 4]))
