from typing import Deque, List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = Deque([start])
        vis = set()

        while q:
            idx = q.popleft()
            val = arr[idx]

            if val == 0:
                return True

            for nxt in (idx - val, idx + val):
                if 0 <= nxt < len(arr) and\
                        nxt not in vis:
                    q.append(nxt)
                    vis.add(nxt)
                    
        return False


s = Solution()
print(s.canReach([4, 2, 3, 0, 3, 1, 2], 5))
