from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []

        for i in range(len(temperatures) - 1):

            t = temperatures[i]
            days = 0

            while t >= temperatures[days + i] and days + i < len(temperatures) - 1:
                days += 1


            if i + days == len(temperatures) and t < temperatures[days + i]:
                days = 0

            res.append(days)

        res.append(0)
        return res


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
