

from typing import Deque, List, Optional
from _utils import TreeNode, build_tree


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left, mid, right = [], [], []
        q = Deque([(root, 0)])

        while q:
            n, mid_offst = q.popleft()
            offst = abs(mid_offst) - 1  # Abs distance in X axis to root - 1

            if mid_offst < 0:
                if len(left) <= offst:
                    left.append([])

                left[offst].append(n.val)
            elif mid_offst > 0:
                if len(right) <= offst:
                    right.append([])

                right[offst].append(n.val)
            else:
                mid.append(n.val)

            if n.left:
                q.append((n.left, mid_offst - 1))

            if n.right:
                q.append((n.right, mid_offst + 1))

        return left[::-1] + [mid] + right


t1 = build_tree([3, 9, 20, None, None, 15, 7])
t2 = build_tree([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])

sol = Solution()
print(sol.verticalOrder(t1))
print(sol.verticalOrder(t2))
