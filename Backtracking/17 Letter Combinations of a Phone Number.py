from typing import List, Set


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyMap = {
            "2": {'a', 'b', 'c'},
            "3": {'d', 'e', 'f'},
            "4": {'g', 'h', 'i'},
            "5": {'j', 'k', 'l'},
            "6": {'m', 'n', 'o'},
            "7": {'p', 'q', 'r', 's'},
            "8": {'t', 'u', 'v'},
            "9": {'w', 'x', 'y', 'z'},
        }

        def backtrack(path: str, dIdx: int, res: List[str]):
            if len(digits) == dIdx:
                return res.append(path)

            for letter in keyMap[digits[dIdx]]:

                # path += letter
                # dIdx += 1

                backtrack(path + letter, dIdx + 1, res)

                # path = path[:-1]
                # dIdx -= 1

            return res

        return backtrack("", 0, [])


sol = Solution().letterCombinations("23")
print(sol)
