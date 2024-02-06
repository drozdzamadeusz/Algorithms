from _utils import Test


class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)
        memo = {LEN: 1}

        def find(i: int) -> int:
            # If already computed, return its value from cache
            if i in memo:
                return memo[i]

            n = int(s[i])
            if n == 0: return 0

            ways = 0

            # Single digit decoding
            ways += find(i + 1)

            # Two digit decoding
            if i + 1 < LEN and int(s[i: i + 2]) in range(10, 27):
                ways += find(i + 2)

            # memo[i] = ways
            return ways

        return find(0)



if __name__ == '__main__':
    fun = Solution().numDecodings

    t = Test(fun)
    t.equal(3, "224")
    t.equal(3, "226")
    t.equal(0, "06")
    t.equal(1836311903, "111111111111111111111111111111111111111111111")
    t.equal(0, "1233213121")
    t.run()


# Without memoization
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
