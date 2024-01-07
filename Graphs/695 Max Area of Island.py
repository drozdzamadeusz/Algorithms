from typing import Deque, List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        vis = set()
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS, COLS = len(grid), len(grid[0])

        def traversal(r, c):
            q = Deque()
            q.append((r, c))
            vis.add((r, c))

            area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in direct:
                    r, c = row + dr, col + dc

                    if r in range(ROWS) and c in range(COLS) and \
                            grid[r][c] == 1 and not (r, c) in vis:
                        q.append((r, c))
                        vis.add((r, c))
                        area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 or (r, c) in vis:
                    continue

                area = traversal(r, c)
                max_area = max(max_area, area)

        return max_area


sol = Solution()
print(sol.maxAreaOfIsland(
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ])
)
