from typing import List

# Varsion 1
#
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def backtrack(path: str, row: int, col: int, idx: int, vis: list[list[bool]]):
#             if path == word:
#                 return True

#             if len(path) >= len(word) or idx >= 0 and word[idx] != path[idx]:
#                 return False

#             choices = []

#             if not path and row == None and col == None:
#                    for rid, r in enumerate(board):
#                     for cid, c in enumerate(board[rid]):
#                         if c == word[0]:
#                             choices.append([rid, cid])
#             else:
#                 if row > 0:
#                     choices.append([row - 1, col])

#                 if row < len(board) - 1:
#                     choices.append([row + 1, col])

#                 if col > 0:
#                     choices.append([row, col - 1])

#                 if col < len(board[0]) - 1:
#                     choices.append([row, col + 1])


#             for [r, c] in choices:
#                 if vis[r][c] == True:
#                     continue

#                 letter = board[r][c]
#                 vis[r][c] = True

#                 if (backtrack(path + letter, r, c, idx + 1, vis)):
#                     return True

#                 vis[r][c] = False

#             return False

#         visited = [[False for _ in range(len(board[0]))]
#                    for _ in range(len(board))]
#         res = backtrack("", None, None, -1, visited)
#         return res


# Version 2
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def backtrack(path: str, row: int, col: int, idx: int, vis: list[list[bool]]):
#             if path == word:
#                 return True

#             if len(path) >= len(word) or word[idx] != path[idx]:
#                 return False

#             choices = []

#             if row > 0:
#                 choices.append([row - 1, col])

#             if row < len(board) - 1:
#                 choices.append([row + 1, col])

#             if col > 0:
#                 choices.append([row, col - 1])

#             if col < len(board[0]) - 1:
#                 choices.append([row, col + 1])

#             for [r, c] in choices:
#                 if vis[r][c] == True:
#                     continue

#                 letter = board[r][c]
#                 vis[r][c] = True

#                 if (backtrack(path + letter, r, c, idx + 1, vis)):
#                     return True

#                 vis[r][c] = False

#             return False

#         visited = [[False for _ in range(len(board[0]))]
#                    for _ in range(len(board))]

#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 w = board[r][c]
#                 visited[r][c] = True

#                 if w == word[0] and backtrack(w, r, c, 0, visited):
#                     return True

#                 visited[r][c] = False

#         return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(path: str, row: int, col: int, idx: int, vis: list[list[bool]]):
            if path == word:
                return True

            if idx + 1 == len(word) or word[idx] != path[idx]:
                return False

            choices = []
            direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in direct:
                if row + dr < 0 or row + dr >= len(board) or \
                        col + dc < 0 or col + dc >= len(board[0]):
                    continue
                choices.append((row+dr, col+dc))

            for r, c in choices:
                if vis[r][c]:
                    continue

                letter = board[r][c]
                vis[r][c] = True

                if (backtrack(path + letter, r, c, idx + 1, vis)):
                    return True

                vis[r][c] = False

            return False

        visited = [[False for _ in range(len(board[0]))]
                   for _ in range(len(board))]

        for r in range(len(board)):
            for c in range(len(board[0])):
                w = board[r][c]
                visited[r][c] = True

                if w == word[0] and backtrack(w, r, c, 0, visited):
                    return True

                visited[r][c] = False

        return False


sol = Solution().exist(
    [["A", "M", "C", "E"],
     ["S", "A", "O", "S"],
     ["A", "D", "R", "E"]],
    "AMADRO")

print(sol)
