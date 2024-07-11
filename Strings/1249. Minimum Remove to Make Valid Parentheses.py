class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_idx = []

        i = 0
        while i < len(s):
            if s[i] == "(":
                open_idx.append(i)
            elif s[i] == ")":
                if open_idx:
                    open_idx.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    continue
            i += 1

        while open_idx:
            i = open_idx.pop()
            s = s[:i] + s[i + 1:]

        return s


sol = Solution()

# print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
print(sol.minRemoveToMakeValid("))(("))
