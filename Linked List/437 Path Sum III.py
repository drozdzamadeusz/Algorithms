from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> int:
        if not root:
            return 0

        def path_from(root: TreeNode, summ: int) -> int:
            if not root:
                return 0
            
            return (summ == root.val) + \
                path_from(root.left, summ - root.val) + \
                path_from(root.right, summ - root.val)

        return path_from(root, summ) + \
            self.pathSum(root.left, summ) + \
            self.pathSum(root.right, summ)


tree1 = TreeNode(val=10,
                 left=TreeNode(val=5,
                               left=TreeNode(val=3,
                                             left=TreeNode(3),
                                             right=TreeNode(-3)),
                               right=TreeNode(val=2,
                                              right=TreeNode(1))),
                 right=TreeNode(val=-3,
                                left=None,
                                right=TreeNode(11)))

sol = Solution().pathSum(tree1, 8)
print(sol)