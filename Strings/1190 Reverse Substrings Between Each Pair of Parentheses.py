
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
                i -= 2  # 2 chars are removed form string (parentheses pair),
                        # thus offset current index by -2 to point to the same location.
            i += 1

        return s


sol = Solution()
print(sol.reverseParentheses("(ed(et(oc))el)"))
print(sol.reverseParentheses("ta()usw((((a))))"))
