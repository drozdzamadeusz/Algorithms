
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rows_chars = {i: set() for i in range(9)}
    cols_chars = {i: set() for i in range(9)}
    boxes_chars = {(i, j): set() for i in range(3) for j in range(3)}

    for r in range(9):
        for c in range(9):
            curr_num = board[r][c]

            if curr_num == ".":
                continue

            if (curr_num in rows_chars[r] or
                curr_num in cols_chars[c] or
                curr_num in boxes_chars[r // 3, c // 3]):
                return False

            rows_chars[r].add(curr_num)
            cols_chars[c].add(curr_num)
            boxes_chars[(r // 3, c // 3)].add(curr_num)
            
    return True


print(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                    ))
