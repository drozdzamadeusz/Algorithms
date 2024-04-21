from typing import Deque, List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid2), len(grid2[0])
        DIRECT = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(r:int, c:int):
            q = Deque([(r, c)])
            grid2[r][c] = 0
            subIsland = 1

            while q:
                row, col = q.popleft()
                
                if grid1[row][col] != 1:
                        subIsland = 0

                for dr, dc in DIRECT:
                    r, c = dr + row, dc + col

                    if 0 <= r < ROWS and 0 <= c < COLS and grid2[r][c]:
                        q.append((r,c))
                        grid2[r][c] = 0

            return subIsland

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c]:
                    islands += bfs(r, c)

        return islands


sol = Solution()
a = sol.countSubIslands(
    grid1=[
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1]
    ],
    grid2=[
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0]
    ]
)
