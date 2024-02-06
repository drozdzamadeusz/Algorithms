from _utils import Test


class Solution:
    def countSubstrings(self, s: str) -> int:
        res, LEN = 0, len(s)

        def find(l: int, r: int):
            nonlocal res
            while l >= 0 and r < LEN and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1

        for i in range(LEN):
            find(i, i)
            find(i, i + 1)

        return res

if __name__ == '__main__':
    sol = Solution()
    test = Test(sol.countSubstrings)

    test.add(3, "abc")
    test.add(6, "aaa")

    test.run()
