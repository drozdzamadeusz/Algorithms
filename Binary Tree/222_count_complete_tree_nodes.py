from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


#       1
#      / \
#     2   5
#    / \   \
#   17  4   6
#          /
#         8
tree1 = TreeNode(1, TreeNode(2, TreeNode(17), TreeNode(4)),
                 TreeNode(5, TreeNode(6, TreeNode(8))))


sol = Solution()
print(sol.countNodes(tree1))