from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(path: str, row: int, col: int, idx: int, vis: list[list[bool]], word: str):
            if path == word:
                return True

            if len(path) >= len(word) or idx >= 0 and word[idx] != path[idx]:
                return False

            choices = []

            if not path and row == None and col == None:
                for rid, r in enumerate(board):
                    for cid, c in enumerate(board[rid]):
                        if c == word[0]:
                            choices.append([rid, cid])
            else:
                direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in direct:
                    if row + dr < 0 or row + dr >= len(board) or \
                            col + dc < 0 or col + dc >= len(board[0]):
                        continue
                    choices.append((row + dr, col + dc))

            for [r, c] in choices:
                if vis[r][c] == True:
                    continue

                letter = board[r][c]
                vis[r][c] = True

                if (backtrack(path + letter, r, c, idx + 1, vis, word)):
                    return True

                vis[r][c] = False

            return False

        res = []

        for w in words:
            visited = [[False for _ in range(len(board[0]))]
                       for _ in range(len(board))]
            if backtrack("", None, None, -1, visited, w):
                res.append(w)

        return res


sol = Solution().findWords(
    [["o", "a", "a", "n"],
     ["e", "t", "a", "e"],
     ["i", "h", "k", "r"],
     ["i", "f", "l", "v"]],
    ["oath", "pea", "eat", "rain"])

print(sol)
