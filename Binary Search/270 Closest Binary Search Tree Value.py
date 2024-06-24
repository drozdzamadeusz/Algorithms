
from typing import Optional
from _utils import TreeNode, build_tree



class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        min_diff, closest = 10 ** 9 + 1, 0

        def dfs(n: Optional[TreeNode]):
            nonlocal min_diff, closest

            if not n:
                return

            diff = abs(n.val - target)

            if diff < min_diff:
                min_diff, closest = diff, n.val

            if target < n.val:
                dfs(n.left)
            else:
                dfs(n.right)

        dfs(root)
        return closest


n = build_tree([4, 2, 5, 1, 3])

sol = Solution()
print(sol.closestValue(n, 3.714286))
