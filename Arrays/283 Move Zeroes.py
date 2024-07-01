from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        LEN = len(nums)
        l = r = 0

        while r < LEN:

            if r > l:
                nums[l] = nums[r]

            if nums[l]:
                l += 1

            r += 1

        for i in range(LEN - (r - l), LEN):
            nums[i] = 0

        print(nums)


sol = Solution()
sol.moveZeroes([-58305, -22022, 0, 0, 0, 0, 0, -76070, 42820,
               48119, 0, 95708, -91393, 60044, 0, -34562, 0, -88974])
