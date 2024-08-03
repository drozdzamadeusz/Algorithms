from typing import List
from _utils import Test


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return 0

        ones = nums.count(1)
        max_window = 0
        ones_window = 0
        l, r = 0, 0

        while r < N * 2:
            ones_window += nums[r % N]
            r += 1

            if r - l > ones:
                ones_window -= nums[l % N]
                l += 1

            if r - l == ones:
                max_window = max(max_window, ones_window)

        return ones - max_window


# s = Solution()
# print(s.minSwaps([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]))

if __name__ == '__main__':
    test = Test(Solution().minSwaps)

    test.add(1, [0, 1, 0, 1, 1, 0, 0])
    test.add(2, [0, 1, 1, 1, 0, 0, 1, 1, 0])
    test.add(0, [1, 1, 0, 0, 1])

    test.run()
