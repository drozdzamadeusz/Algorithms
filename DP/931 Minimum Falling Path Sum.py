# import math
# from typing import List

# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         if not matrix or not matrix[0]:
#             return 0

#         ROWS, COLS = len(matrix), len(matrix[0])

#         min_dist = math.inf

#         def travel(r: int, c: int, dist: int):
#             nonlocal min_dist
#             if r == ROWS - 1:
#                 min_dist = min(min_dist, dist + matrix[r][c])
#                 return

#             for dr, dc in [(r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
#                 if dr not in range(ROWS) or dc not in range(COLS):
#                     continue

#                 travel(dr, dc, dist + matrix[r][c])

#         for c in range(COLS):
#             travel(0, c, 0)

#         return min_dist


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(1, ROWS):
            for c in range(COLS):
                above = set()
                for dr, dc in ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1)):
                    if dr in range(ROWS) and dc in range(COLS):
                        above.add(matrix[dr][dc])

                matrix[r][c] += min(above)

        return min(matrix[ROWS - 1])


sol = Solution()
print(sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(sol.minFallingPathSum([[-19, 57], [-40, -5]]))
