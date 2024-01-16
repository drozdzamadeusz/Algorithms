from typing import Deque, List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        on_edge = set()

        for r in range(ROWS):
            if board[r][0] == "O":
                on_edge.add((r, 0))
            if board[r][COLS - 1] == "O":
                on_edge.add((r, COLS - 1))

        for c in range(COLS):
            if board[0][c] == "O":
                on_edge.add((0, c))
            if board[ROWS - 1][c] == "O" and (ROWS - 1, c):
                on_edge.add((ROWS - 1, c))

        excluded = set()

        def explore(row: int, col: int):
            excluded.add((row, col))

            for r, c in [(row + 1, col), (row - 1, col),(row, col + 1), (row, col - 1)]:
                if (r in range(ROWS)
                    and c in range(COLS)
                    and board[r][c] == "O"
                    and (r, c) not in excluded
                ):
                    explore(r, c)

        for r, c in on_edge:
            explore(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in excluded:
                    board[r][c] = "X"


sol = Solution()
print(
    sol.solve(
        board=[
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)
