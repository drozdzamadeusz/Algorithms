from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(l: int, r: int, x: int, lBiased: bool):
            if l > r:
                return -1

            m = (l + r) // 2

            if x == nums[m]:
                return m

            if x < nums[m]:
                return search(l, m - 1, x, lBiased)

            return search(m + 1, r, x, lBiased)

        return search(0, len(nums) - 1, target, False)


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
