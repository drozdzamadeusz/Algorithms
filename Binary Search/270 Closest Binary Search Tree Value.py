
from typing import Optional
from _utils import TreeNode, build_tree



class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        min_diff, closest = 10 ** 9 + 1, 0

        def dfs(node: Optional[TreeNode]):
            nonlocal min_diff, closest

            if not node:
                return

            diff = abs(node.val - target)

            if diff < min_diff:
                min_diff, closest = diff, node.val

            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)
        return closest


n = build_tree([4, 2, 5, 1, 3])

sol = Solution()
print(sol.closestValue(n, 3.714286))
