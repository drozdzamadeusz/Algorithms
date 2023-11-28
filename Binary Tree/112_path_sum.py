import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum and not root.right and not root.left:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or \
            self.hasPathSum(root.right, targetSum - root.val)


#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(5, TreeNode(6, TreeNode(8))))


sol = Solution()
print(sol.hasPathSum(tree1, 12))
