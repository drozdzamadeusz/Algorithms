from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        cache = {}

        def dp(r: int, c: int):
            if (r, c) in cache:
                return cache.get((r, c))

            if c == 0 or r == 0: # Base case 1: No path if height or width of grid equals 0
                return 0

            if obstacleGrid[r - 1][c - 1] == 1: # Base case 2: No path if obstacle is in the bottom-right corner
                return 0

            if c == r == 1: # Base case 3: In a 1 x 1 grid, there is 1 path
                return 1

            cache[(r, c)] = dp(r - 1, c) + dp(r, c - 1)
            return cache[(r, c)]

        return dp(len(obstacleGrid), len(obstacleGrid[0]))


sol = Solution()
# print(sol.uniquePathsWithObstacles([
#     [0, 0, 0],
#     [0, 0, 1],
#     [0, 0, 0]]))
# print(sol.uniquePathsWithObstacles([
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]]))

print(sol.uniquePathsWithObstacles([
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 0],
]))
