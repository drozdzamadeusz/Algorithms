from typing import Deque, List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = Deque()
        fresh, time = 0, 0

        def traversal():
            nonlocal time, fresh, q

            while q and fresh > 0:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    for dr, dc in direct:
                        r, c = dr + row, dc + col

                        if r not in range(ROWS) or c not in range(COLS) or\
                            grid[r][c] != 1:
                            continue
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
                        
                time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        traversal()

        return time if fresh == 0 else -1


sol = Solution()
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
