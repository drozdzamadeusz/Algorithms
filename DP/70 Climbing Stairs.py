# class Solution:
#     def __init__(self) -> None:
#         self.memo = {}

#     def climbStairs(self, n: int) -> int:
#         if n < 2:
#             return 1

#         memo = self.memo

#         if n not in memo:
#             memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#         return memo[n]

class Solution:

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one


sol = Solution()
print(sol.climbStairs(5))
