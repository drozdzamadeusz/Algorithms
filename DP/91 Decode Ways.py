from _utils import Test


class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)
        memo = [0] * LEN

        def find(i: int) -> int:
            if i == LEN:
                return 1

            # If we've already computed this, return its value from cache
            if memo[i]:
                return memo[i]

            opts = []
            n = int(s[i])

            # Single digit decoding
            if n in range(1, 10):
                opts.append((n, 1))

            # Two digit decoding
            if n in range(1, 3) and i + 1 < LEN:
                twoDig = int(s[i: i + 2])
                if twoDig in range(10, 27):
                    opts.append((twoDig, 2))

            ways = 0
            for (_n, idx) in opts:
                ways += find(idx + i)

            memo[i] = ways
            return ways

        return find(0)


fun = Solution().numDecodings
t = Test()
t.add(fun("12"), 2)
t.add(fun("226"), 3)
t.add(fun("06"), 0)
t.add(fun("2134321412312322223"))
t.add(fun("111111111111111111111111111111111111111111111"), 1836311903)
t.run()


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         LEN = len(s)

#         def find(i: int) -> int:
#             if i == LEN: return 1

#             n = int(s[i])
#             nxt_1 = int(s[i + 1]) if i + 1 < LEN else None
#             nxt_2 = int(s[i + 2]) if i + 2 < LEN else None

#             opts = []

#             if n in range(1, 10):
#                 opts.append((n, 1))

#             if n in range(1, 3) and nxt_1 != None and nxt_2 != 0:
#                 twoDigs = int(s[i: i + 2])
#                 if twoDigs in range(10, 27):
#                     opts.append((twoDigs, 2))

#             ways = 0
#             for (_n, idx) in opts:
#                 ways += find(idx + i)
#             return ways

#         return find(0)
