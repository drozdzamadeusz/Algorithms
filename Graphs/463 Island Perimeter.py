from typing import Deque, List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECT = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # def bfs(r, c):
        #     perimeter = 0
        #     q = Deque([(r, c)])
        #     vis = set()

        #     while len(q):
        #         row, col = q.popleft()

        #         for dr, dc in DIRECT:
        #             r, c = row + dr, col + dc

        #             if r < 0 or c < 0 or r == ROWS or c == COLS:
        #                 perimeter += 1  # increment perimeter if cell is on the border
        #             else:
        #                 if grid[r][c] == 0:
        #                     perimeter += 1  # increment perimeter if next cell is water
        #                 elif (r, c) not in vis and (r, c) not in q:
        #                     q.append((r, c))
        #         vis.add((row, col))
        #     return perimeter

        def dfs(row, col):
            perimeter = 0
            grid[row][col] = -1

            for dr, dc in DIRECT:
                r, c = row + dr, col + dc

                if r < 0 or c < 0 or r == ROWS or c == COLS:
                    perimeter += 1
                else:
                    if grid[r][c] == 0:
                        perimeter += 1  # increment perimeter if next cell is water
                    elif grid[r][c] == 1:
                        grid[r][c] = -1
                        perimeter += dfs(r, c)
            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)


sol = Solution()
print(sol.islandPerimeter
      (
          [[1, 1], [1, 1]]

      ))
