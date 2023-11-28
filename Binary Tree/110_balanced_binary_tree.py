import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(root: Optional[TreeNode]):
            if not root:
                return 0

            return 1 + max(depth(root.left), depth(root.right))

        return abs(depth(root.left) - depth(root.right)) < 2 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right)


#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(5, TreeNode(6, TreeNode(8))))


sol = Solution()
print(sol.isBalanced(tree1))
