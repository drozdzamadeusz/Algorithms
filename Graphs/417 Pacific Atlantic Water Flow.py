from typing import Deque, List, Set


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         ROWS, COLS = len(heights), len(heights[0])

#         res = []

#         direct = ((-1, 0), (0, -1), (1, 0), (0, 1))

#         def dfs(row: int, col: int):
#             pacific, atlantic = False, False

#             vis = set([(row, col)])
#             q = Deque([(row, col)])

#             while q:
#                 row, col = q.pop()

#                 for dr, dc in direct:
#                     r, c = row + dr, col + dc

#                     if r < 0 or c < 0:
#                         pacific = True
#                     elif r >= ROWS or c >= COLS:
#                         atlantic = True

#                     if pacific and atlantic:
#                         return True

#                     if (
#                         r not in range(ROWS)
#                         or c not in range(COLS)
#                         or (r, c) in vis
#                         or heights[r][c] > heights[row][col]
#                     ):
#                         continue

#                     q.append((r, c))
#                     vis.add((r, c))

#             return pacific and atlantic

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if dfs(r, c):
#                     res.append([r, c])

#         return res


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        direct = ((-1, 0), (0, -1), (1, 0), (0, 1))

        def dfs(q: Deque, vis: Set):
            res = []

            while q:
                row, col = q.pop()
                res.append((row, col))
                for dr, dc in direct:
                    r, c = row + dr, col + dc

                    if (
                        r not in range(ROWS)
                        or c not in range(COLS)
                        or (r, c) in vis
                        or heights[row][col] > heights[r][c]
                    ):
                        continue

                    q.append((r, c))
                    vis.add((r, c))
            return res

        q, vis = Deque(), set()

        for r in range(ROWS):
            q.append((r, 0))
            vis.add((r, 0))

        for c in range(COLS):
            if c != 0:
                q.append((0, c))
                vis.add((0, c))

        pacific = dfs(q, vis)

        q, vis = Deque(), set()

        for r in range(ROWS):
            q.append((r, COLS - 1))
            vis.add((r, COLS - 1))

        for c in range(COLS):
            if c != COLS:
                q.append((ROWS - 1, c))
                vis.add((ROWS -1, c))

        arctic = dfs(q, vis)


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in arctic:
                    res.append([r,c])

        return res


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
sol = Solution()
print(sol.pacificAtlantic(heights))
