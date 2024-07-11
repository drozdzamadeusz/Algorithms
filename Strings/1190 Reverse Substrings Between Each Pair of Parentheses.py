from typing import Deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        opens_idx = []
        i = 0

        while i < len(s):
            if s[i] == "(":
                opens_idx.append(i)
            elif s[i] == ")":
                o_idx = opens_idx.pop()
                sub_s = s[o_idx + 1:i][::-1]
                s = s[:o_idx] + sub_s + s[i + 1:]
                i -= 2 # parentheses pair is removed, which is two charters after current index, thus decrement index by 2, 
            i += 1

        return s


sol = Solution()
# print(sol.reverseParentheses("(ed(et(oc))el)"))
print(sol.reverseParentheses("ta()usw((((a))))"))
