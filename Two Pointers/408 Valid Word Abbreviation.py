from _utils import Test


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        W_LEN, A_LEN = len(word), len(abbr)
        l = abbr_sum = 0

        while l < A_LEN:
            if abbr[l] == '0' and \
               (l == 0 or not abbr[l - 1].isdigit()):
                return False                           # Leading Zero found

            if abbr_sum >= W_LEN:
                return False                           # Abbr sum greater than word length

            if abbr[l].isdigit():
                r = l
                while r + 1 < A_LEN and abbr[r + 1].isdigit():
                    r += 1

                abbr_sum += int(abbr[l: r + 1])
                l = r
            else:
                if word[abbr_sum] != abbr[l]:           # Chars in abbr and word don't match
                    return False

                abbr_sum += 1

            l += 1

        return W_LEN == abbr_sum


# sol = Solution()
# print(sol.validWordAbbreviation("internationalization", "i12iz4n"))
# print(sol.validWordAbbreviation("hi", "2i"))

if __name__ == '__main__':
    test = Test(Solution().validWordAbbreviation)

    test.add(True, "internationalization", "i12iz4n")
    test.add(False, "hi", "2i")
    test.add(False, "apple", "a2e")

    test.run()
