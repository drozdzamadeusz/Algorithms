from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        preProduct, postProduct = [1] * LEN, [1] * LEN

        preProduct[0] = nums[0]
        postProduct[-1] = nums[-1]

        for i in range(1, LEN):
            preProduct[i] = nums[i] * preProduct[i - 1]

        for i in range(LEN - 2, -1, -1):
            postProduct[i] = nums[i] * postProduct[i + 1]

        for i in range(LEN):
            nPre = 1
            if i > 0:
                nPre = preProduct[i - 1]

            nPost = 1
            if i < LEN - 1:
                nPost = postProduct[i + 1]

            nums[i] = nPre * nPost

        return nums

sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
