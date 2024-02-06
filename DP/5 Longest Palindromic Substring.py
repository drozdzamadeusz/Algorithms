from _utils import Test


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, LEN = '', len(s)

        # Finds the longest palindrome by expanding around the center (l, r)
        def longest_pal(l: int, r: int) -> str:
            pal = ''
            while l >= 0 and r < LEN and s[l] == s[r]:
                pal = s[l: r + 1]
                l, r = l - 1, r + 1
            return pal

        # Returns the longer of two strings
        str_max = lambda s1, s2: s1 if len(s1) >= len(s2) else s2

        for i in range(LEN):
            odd = longest_pal(i, i)
            even = longest_pal(i, i + 1)
            longer = str_max(odd, even)
            
            res = str_max(res, longer)

        return res

if __name__ == '__main__':
    sol = Solution()
    test = Test(sol.longestPalindrome)
    test.equal( "bab", "babad",)
    test.equal("bb", "cbbd")
    test.run()
