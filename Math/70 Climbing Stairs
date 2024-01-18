class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        memo = self.memo

        if n not in memo:
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return memo[n]


sol = Solution()
print(sol.climbStairs(3))
