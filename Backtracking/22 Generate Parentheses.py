from typing import List, Set


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(path: str, opened: int, closed: int):
            if len(path) == n * 2:
                return [path]

            opts = {'(', ')'}

            if opened == 0 or opened == closed:
                opts = {'('}
            elif opened == n:
                opts = {')'}

            res = []
            for opt in opts:
                new_opened = opened + 1 if opt == '(' else opened
                new_closed = closed + 1 if opt == ')' else closed
                new_path = path + opt

                res.extend(backtrack(new_path, new_opened, new_closed))

            return res

        return backtrack("", 0, 0)


sol = Solution().generateParenthesis(3)
print(sol)
