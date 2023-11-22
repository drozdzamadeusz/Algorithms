import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):
        if not root:
            return -math.inf

        if not root.right and not root.left:
            return root.val

        left = self.maxPathSum(root.left)
        right = self.maxPathSum(root.right)

        return max(left, right) + root.val


#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(5, TreeNode(6)))


#       1
tree2 = TreeNode(1)


#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))


sol = Solution()
print(sol.maxPathSum(tree1))