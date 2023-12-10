import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], minVal: Optional[int], maxVal: Optional[int]):
            if not node:
                return True

            if minVal != None and node.val >= minVal:
                return False

            if maxVal != None and node.val <= maxVal:
                return False

            return isValid(node.left, node.val, maxVal) and isValid(node.right, minVal, node.val)

        return isValid(root, None, None)


tree3 = TreeNode(val=0, left=None, right=TreeNode(-1))

tree = TreeNode(
    val=5,
    left=TreeNode(val=4),
    right=TreeNode(val=6,
                   left=TreeNode(3), right=TreeNode(7)),
)


#       2
#      / \
#     1   3
tree1 = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))

#       4
#      / \
#     2   5
#    / \   \
#   1   3   6
tree2 = TreeNode(
    val=4,
    left=TreeNode(val=2, left=TreeNode(1), right=TreeNode(3)),
    right=TreeNode(val=5, right=TreeNode(6)),
)


sol = Solution()
print(sol.isValidBST(tree3))
