from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 1, 1

        while (r < len(nums)):
            if(nums[r] != nums[r - 1]):
                nums[l] = nums[r]
                l += 1

            r += 1

        return l

sol = Solution()
print(sol.removeDuplicates([0, 0, 1]))

# [1, 2, 3]

# [1, 1, 2, 2, 3, 3]
#       /\


# [1, 2, 2, 2, 3, 3]
#             /\

