from typing import List


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         LEN = len(height)
#         l = water = 0

#         while l < LEN - 2:
#             r = tallest = l + 1

#             while r < LEN:          # Find highest elevation to trap water from the right side.
#                 if height[r] >= height[l]:
#                     break
#                 if height[r] > height[tallest]:
#                     tallest = r
#                 if r + 1 == LEN:
#                     r = tallest
#                     break
#                 r += 1

#             min_h = min(height[l], height[r])

#             if r - l > 1 and min_h > 0:
#                 for i in range(l + 1, r):
#                     water += min_h - height[i]

#             l = r

#         return water


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        water = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                water += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water += rMax - height[r]

        return water


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
