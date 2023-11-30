from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


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
print(sol.pathSum(tree1, 20))
