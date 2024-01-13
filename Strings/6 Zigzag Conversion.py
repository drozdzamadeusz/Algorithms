from typing import Deque


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows < 2:
#             return s

#         LEN, DIST = len(s), numRows + numRows - 2

#         q, added = Deque(), set()
#         res = ""

#         for i in range(0, LEN, DIST):
#             q.append(i)
#             added.add(i)

#         while q:
#             i = q.popleft()
#             res += s[i]

#             if i - 1 in range(LEN) and not i - 1 in added:
#                 q.append(i - 1)
#                 added.add(i - 1)

#             if i + 1 in range(LEN) and not i + 1 in added:
#                 q.append(i + 1)
#                 added.add(i + 1)

#         return res


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows < 2 or numRows >= len(s):
#             return s

#         LEN, DIST = len(s), numRows + numRows - 2
#         q = Deque()
#         res = ""

#         for row in range(numRows):
#             for i in range(row, LEN, DIST):
#                 q.append(i)
#                 next = i + (numRows - 1 - row) * 2
#                 if row != 0 and row != numRows - 1 and next < LEN:
#                     q.append(next)

#         while q:
#             res += s[q.popleft()]

#         return res


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 or numRows >= len(s):
            return s

        LEN, STEP = len(s), numRows + numRows - 2
        res = ""

        for row in range(numRows):
            for i in range(row, LEN, STEP):
                res += s[i]
                next = i + (numRows - 1 - row) * 2
                if row != 0 and row != numRows - 1 and next < LEN:
                    res += s[next]

        return res


sol = Solution()
print(sol.convert("PAYPALISHIRINGRIGHTNOW", 4) == "PINTALSIGHNYAHRRGOPIIW")
