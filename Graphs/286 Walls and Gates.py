from typing import Deque, List
from _utils import Test


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])

        def explore(row: int, col: int):
            nonlocal rooms

            vis = set([(row, col)])
            q = Deque([(row, col, 0)])

            while q:
                r, c, dst = q.popleft()

                if dst < rooms[r][c]:
                    rooms[r][c] = dst

                for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= dr < ROWS and \
                            0 <= dc < COLS and \
                            rooms[dr][dc] > 0 and \
                            rooms[dr][dc] > dst + 1 and \
                            (dr, dc) not in vis:
                        q.append((dr, dc, dst + 1))
                        vis.add((dr, dc))

            return

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    explore(r, c)
        return rooms


if __name__ == '__main__':
    fun = Solution().wallsAndGates
    test = Test(fun)
    expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    arg = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    test.equal(expected, arg)

    arg = [[-1]]
    expected = [[-1]]
    test.equal(arg, expected)

    test.run()
