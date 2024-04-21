class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dp(r: int, c: int):
            if (r, c) in cache:
                return cache.get((r, c))

            if (c, r) in cache:
                return cache.get((c, r))

            if c == 0 or r == 0:
                return 0
            if c == r == 1:
                return 1

            cache[(r, c)] = dp(r - 1, c) + dp(r, c - 1)
            return cache[(r, c)]

        return dp(m, n)


sol = Solution()
print(sol.uniquePaths(3, 3))
