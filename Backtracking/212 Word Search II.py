from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        found = set()
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(path: str, row: int, col: int, node: TrieNode):
            if node.isEnd:
                found.add(path)

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '#':
                return

            temp = board[row][col]
            board[row][col] = '#'
            node = node.children.get(temp)

            if node:
                for dr, dc in direct:
                    backtrack(path + temp, row + dr, col + dc, node)

            board[row][col] = temp

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.children:
                    backtrack("", row, col, trie.root)

        return list(found)


sol = Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], [
    "i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"])


# sol = Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
#                            ["oath", "pea", "eat", "rain", "oathi", "oathk",
#                                "oathf", "oate", "oathii", "oathfi", "oathfii"]
#                            )


# sol = Solution().findWords(
#     [["o", "a", "a", "n"],
#      ["o", "t", "a", "e"],
#      ["a", "h", "k", "r"],
#      ["a", "f", "l", "v"]],
#     ["oa", "oaa"])

print(sol)
