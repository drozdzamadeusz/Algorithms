from typing import Deque, List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(land), len(land[0])
        DIRECT = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def bfs(r: int, c: int):
            q = Deque([(r, c)])
            land[r][c] = 0
            last = None

            while q:
                row, col = q.popleft()
                last = [row, col]

                for dr, dc in DIRECT:
                    r, c = dr + row, dc + col

                    if 0 <= r < ROWS and 0 <= c < COLS and land[r][c]:
                        q.append((r, c))
                        land[r][c] = 0
            return last

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c]:
                    result.append([r, c] + bfs(r, c))
        return result

sol = Solution()
print(sol.findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
