from typing import Deque, List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        last_idx = len(nums) - 1
        q = Deque([(0, 0)])

        dist = [-1] * len(nums)

        while q:
            idx, jumps = q.popleft()
            jump_len = nums[idx]

            jumps += 1
            for stp in range(1, jump_len + 1):
                nxt_pos = idx + stp

                if nxt_pos > last_idx:
                    continue

                if dist[nxt_pos] <= jumps and dist[nxt_pos] != -1:
                    continue

                dist[nxt_pos] = jumps

                if nxt_pos != last_idx:
                    q.append((nxt_pos, jumps))

        return dist[-1]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
