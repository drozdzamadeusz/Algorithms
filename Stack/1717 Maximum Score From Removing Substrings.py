# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         res, i = 0, 0

#         prev_is_char = False

#         while i < len(s) - 1:

#             if x >= y:
#                 c1, c2 = 'a', 'b'
#             else:
#                 c1, c2 = 'b', 'a'

#             if s[i] == c1 and s[i + 1] == c2:
#                 res += y
#             elif s[i] == c2 and s[i + 1] == c1:
#                 res += x
#             else:
#                 prev_is_char = s[i] == c1 or s[i] == c2
#                 i += 1
#                 continue

#             s = s[:i] + s[i + 2:]

#             print(f'{s[:i]}{c1.capitalize()}{c2.capitalize()}{s[i + 2:]}')

#             if prev_is_char:
#                 i -= 1

#         print(s, res)
#         return res


from typing import Deque


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove(ch1: str, ch2: str) -> int:
            nonlocal s
            count = 0
            stack = []

            for c in s:
                if stack and stack[-1] == ch1 and c == ch2:
                    stack.pop()
                    count += 1
                else:
                    stack.append(c)

            s = "".join(stack)
            return count

        ch1, ch2 = 'a', 'b'
        if y > x:
            ch1, ch2, x, y = ch2, ch1, y, x

        return remove(ch1, ch2) * x + remove(ch2, ch1) * y


sol = Solution()
# print(sol.maximumGain(s="abab", x=1, y=10))
print(sol.maximumGain(s="cdbcbbaaabab", x=5, y=4))
