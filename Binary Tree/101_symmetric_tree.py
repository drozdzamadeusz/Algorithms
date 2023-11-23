from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSym(left:  Optional[TreeNode], right:  Optional[TreeNode]):
            if not left or not right:
                return left == right

            return left.val == right.val and \
                isSym(left.left, right.right) and \
                isSym(left.right, right.left)

        return isSym(root, root)


#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(5, TreeNode(6)))

#         1
#       /   \
#      2     2
#    / \    / \
#       4  4
tree2 = TreeNode(1, TreeNode(2, right=TreeNode(4)),
                 TreeNode(2, left=TreeNode(4)))


sol = Solution()
print(sol.isSymmetric(tree2))
