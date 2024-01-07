from typing import Deque, List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        vis = set()
        res = 0

        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def traversal(row, col):
            q = Deque()
            q.append((row, col))
            vis.add((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in direct:
                    row, col = r + dr, c + dc

                    if row in range(ROWS) and col in range(COLS) and \
                            grid[row][col] == "1" and (row, col) not in vis:
                        q.append((row, col))
                        vis.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in vis:
                    res += 1
                    traversal(r, c)

        return res


sol = Solution()
print(sol.numIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
))
