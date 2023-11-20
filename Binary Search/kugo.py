from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while (l <= r):
            k = (l + r) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / k)

            if (time <= h):
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1

        return res


solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))
