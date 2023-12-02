from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return root.val

        def sum(node: Optional[TreeNode]):
            if not node:
                return 0

            leafVal = 0
            if node.left and not node.left.left and not node.left.right:
                leafVal += node.left.val

            return leafVal + sum(node.left) + sum(node.right)

        return sum(root)


#       1
#      / \
#     2   5
#    / \   \
#   17  4   6
#          /
#         8
#        /
#       3
tree1 = TreeNode(1, TreeNode(2, TreeNode(17), TreeNode(4)),
                 TreeNode(5, right=TreeNode(6, left=TreeNode(8, left=TreeNode(20)))))


#       3
#      / \
#     9  20
#        / \
#       15  7
tree2 = TreeNode(3, left=TreeNode(9), right=TreeNode(
    20, left=TreeNode(15), right=TreeNode(7)))

#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))


sol = Solution()
print(sol.sumOfLeftLeaves(tree2))
