from _utils import Test


class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)

        def find(i: int) -> int:
            if i == LEN: return 1

            n = int(s[i])
            nxt_1 = int(s[i + 1]) if i + 1 < LEN else None
            nxt_2 = int(s[i + 2]) if i + 2 < LEN else None

            opts = []

            if n in range(1, 10):
                opts.append((n, 1))

            if n in range(1, 3) and nxt_1 != None and nxt_2 != 0:
                twoDigs = int(s[i: i + 2])
                if twoDigs in range(10, 27):
                    opts.append((twoDigs, 2))

            ways = 0
            for (_n, idx) in opts:
                ways += find(idx + i)
            return ways

        return find(0)



t = Test(Solution().numDecodings)
t.add(t.fun("225"), 3)
t.add(t.fun("225"), 3)
t.add(t.fun("06"), 0)
t.add(t.fun("2134321412312322223"))
# t.add(sol("111111111111111111111111111111111111111111111"), 1836311903)
t.run()
