class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = {}

        for l in s:
            if l not in s_count:
                s_count[l] = 0
            s_count[l] += 1

        steps = 0

        for l in t:
            if l not in s_count:
                steps += 1
                continue
            s_count[l] -= 1
            if s_count[l] < 0:
                steps += 1

        return steps


sol = Solution()
print(sol.minSteps("bab", "aba"))
