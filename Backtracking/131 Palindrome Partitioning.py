from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1

            return True

        def backtrack(path: List[int], start: int):
            if start == len(s):
                return [path]

            res = []
            
            for i in range(start, len(s)):
                frag = s[start:i + 1]

                if is_palindrome(frag):
                    res.extend(backtrack(path + [frag], i + 1))

            return res

        return backtrack([], 0)


sol = Solution()
res = sol.partition("aab")
print(res)
