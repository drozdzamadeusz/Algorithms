from typing import List
from _utils import Test


class Solution:
    def rob(self, nums: List[int]) -> int:
        LEN = len(nums)
        if LEN == 1: return nums[0]

        def rob(idx_s, idx_e):
            LEN = idx_e - idx_s

            fst = nums[idx_s]
            if LEN == 1: return nums[idx_s]

            sec = nums[idx_s + 1]
            if LEN == 2: return max(fst, sec)

            # House that have to be skipped in next iteration
            prev = nums[idx_s + 2] + fst

            # [fst, sec, prev, i, i + 1]
            for i in range(3 + idx_s, idx_e):
                if (fst > sec):
                    res = fst + nums[i]
                    sec = prev
                else:
                    res = sec + nums[i]
                    fst = prev
                prev = res
            return max(fst, sec, prev)

        return max(rob(1, LEN), rob(0, LEN - 1))


if __name__ == '__main__':
    sol = Solution()
    test = Test(sol.rob)

    test.equal(4, [1, 2, 3, 1])
    test.equal(4, [1, 2, 3, 1])
    test.equal(3, [1, 2, 3])

    test.run()
