from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        LEN = len(height)
        l = water = 0

        while l < LEN - 2:
            r = tallest = l + 1

            while r < LEN:          # Find highest elevation to trap water from the right side.
                if height[r] >= height[l]:
                    break
                if height[r] > height[tallest]:
                    tallest = r
                if r + 1 == LEN:
                    r = tallest
                    break
                r += 1

            min_h = min(height[l], height[r])

            if r - l > 1 and min_h > 0:
                for i in range(l + 1, r):
                    water += min_h - height[i]

            l = r

        return water


# Find two tallest, and count water then next two tallest...


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         LEN = len(height)

#         l_max, r_max = 0, 0
#         l_max_idx, r_max_idx = 0, 0

#         l, r = 0, LEN - 1

#         l_max_next, r_min_next = LEN - 1, 0

#         # find highest elevations

#         while True:
#             while l < r:
#                 if l < l_max_next and\
#                         l_max < height[l]:
#                     l_max = height[l]
#                     l_max_idx = l
#                 if r > r_min_next and \
#                         r_max < height[r]:
#                     r_max = height[r]
#                     r_max_idx = r

#                 if l >= l_max_next and\
#                         r <= r_min_next:
#                     break
#                 l += 1
#                 r -= 1

#             l_max_next, r_min_next = l_max_idx, r_max_idx

#             if l_max == 0 or r_max == 0:
#                 break

#             l_max, r_max = 0, 0
#             l_max_idx, r_max_idx = 0, 0
#             l, r = 0, LEN - 1

#         return 0


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
