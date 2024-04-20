from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def explore(r, c, add_diagonally: set, sub_diagonally: set, columns: set, left: int):
            if (r + c) in add_diagonally or \
                (r - c) in sub_diagonally or \
                    c in columns:
                return

            add_diagonally.add(r + c)
            sub_diagonally.add(r - c)
            columns.add(c)

            left -= 1
            res_row = ['.' * c + 'Q' + '.' * (n - c - 1)]

            if left == 0:
                return res_row

            for col in range(n):

                result = explore(r + 1, col, add_diagonally,
                                 sub_diagonally, columns, left)
                if result and len(result) == left:
                    res_row.extend(result)

            return res_row

        result = []
        for c in range(n):
            res = explore(0, c, set(), set(), set(), n)
            if len(res) == n:
                result.append(res)

        return result



sol = Solution()
print(sol.solveNQueens(4))
