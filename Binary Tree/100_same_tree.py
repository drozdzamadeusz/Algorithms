
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not q or not p:
            return q is p
            
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return p.val == q.val and left and right


tree1 = TreeNode(1, TreeNode(left=2))


tree2 = TreeNode(1, TreeNode(right=2))


sol = Solution()

print(sol.isSameTree(tree1, tree2))
