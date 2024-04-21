class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def paths(m: int, n: int):
            if (m, n) in cache:
                return cache.get((m, n))

            if (n, m) in cache:
                return cache.get((n, m))

            if n == 0 or m == 0:
                return 0
            if n == m == 1:
                return 1

            cache[(n, m)] = paths(m - 1, n) + paths(m, n - 1)

            return cache[(n, m)]

        return paths(m, n)


sol = Solution()
print(sol.uniquePaths(3, 3))
