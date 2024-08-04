import random
from typing import List

from _utils import Test


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


if __name__ == '__main__':
    test = Test(Solution().canJump, timeout=1000,
                mode='execution_time', output='console_minimal')

    test.add(True, [2, 3, 1, 1, 4])
    test.add(False, [3, 2, 1, 0, 4])
    test.add(False, [2, 3, 1, 1, 4])
    test.add(False, [3, 2, 1, 0, 4])

    random.seed(10)
    for _ in range(6):
        size = random.randint(50000, 100000)
        array = [random.randint(0, 250) for _ in range(size)]
        test.add(True, array)

    test.run()
