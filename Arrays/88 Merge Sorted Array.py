from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = n + m - 1

        while n:
            if m and nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1

            i -= 1

        # print(nums1)


sol = Solution()
# print(sol.merge(
#     nums1=[7, 7, 7, 0, 0, 0],
#     m=3,
#     nums2=[6, 6, 6],
#     n=3)
# )

print(sol.merge(
    nums1=[6, 6, 6, 0, 0, 0],
    m=3,
    nums2=[7, 7, 7],
    n=3)
)


# print(sol.merge(
#     nums1=[2, 0],
#     m=1,
#     nums2=[1],
#     n=1)
# )

# print(sol.merge(
#     nums1=[2, 0],
#     m=1,
#     nums2=[1],
#     n=1)
# )
