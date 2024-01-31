from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(0, len(cost) - 2):
            idx = len(cost) - 3 - i
            next_1 = cost[idx + 1]
            next_2 = cost[idx + 2]

            cost[idx] += min(next_1, next_2)

        return min(cost[0], cost[1])


sol = Solution()
print(sol.minCostClimbingStairs([10, 15, 20, 40]))
