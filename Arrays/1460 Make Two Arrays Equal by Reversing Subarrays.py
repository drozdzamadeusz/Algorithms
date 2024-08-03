from typing import Counter, List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


s = Solution()
print(s.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
