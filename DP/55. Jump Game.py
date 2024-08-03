from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        last_idx = len(nums) - 1
        vis = {0}

        while vis:
            idx = vis.pop()
            jump = nums[idx]

            for stp in range(1, jump + 1):
                nxt_pos = idx + stp

                if nxt_pos == last_idx:
                    return True
                elif nxt_pos > last_idx:
                    continue

                vis.add(nxt_pos)

        return False


s = Solution()
print(s.canJump([0]))
