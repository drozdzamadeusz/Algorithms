from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def god_count(node: Optional[TreeNode], max_curr: int):
            if not node:
                return 0

            max_new = max(node.val, max_curr)

            return (1 if node.val >= max_curr else 0) + \
                god_count(node.left, max_new) + \
                god_count(node.right, max_new)

        return 1 + god_count(root.left, root.val) + god_count(root.right, root.val)


#       3
#      / \
#     1   4
tree1 = TreeNode(val=3,
                 left=TreeNode(val=1),
                 right=TreeNode(val=4))

#       3
#      / \
#     1   4
#    / \   \
#   3   1   5
tree2 = TreeNode(val=3,
                 left=TreeNode(val=4,
                               left=TreeNode(3), right=TreeNode(1)),
                 right=TreeNode(val=1,
                                right=TreeNode(5)))


tree3 = TreeNode(val=2,
                 left=None,
                 right=TreeNode(val=4,
                                left=TreeNode(10),
                                right=TreeNode(val=8,
                                               left=TreeNode(4),
                                               right=None)))


sol = Solution()
print(sol.goodNodes(tree3))
