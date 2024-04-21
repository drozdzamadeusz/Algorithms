from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(row, col, columns, add_diagonally, sub_diagonally):
            return not (col in columns or (row + col) in add_diagonally or (row - col) in sub_diagonally)

        def explore(r, columns: set, add_diagonally: set, sub_diagonally: set, solution: List[str]):
            if r == n:
                result.append(solution[:])
                return

            for c in range(n):
                if isSafe(r, c, columns, add_diagonally, sub_diagonally):

                    columns.add(c)
                    add_diagonally.add(r + c)
                    sub_diagonally.add(r - c)
                    solution.append('.' * c + 'Q' + '.' * (n - c - 1))

                    explore(r + 1, columns, add_diagonally,
                            sub_diagonally, solution)

                    columns.remove(c)
                    add_diagonally.remove(r + c)
                    sub_diagonally.remove(r - c)
                    solution.pop()

        result = []
        explore(0, set(), set(), set(), [])

        return result


sol = Solution()
print(sol.solveNQueens(5))
