from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetNum: int) -> int:
        if not root:
            return 0

        def path_from(root: TreeNode, target: int) -> int:
            if not root:
                return 0
            
            return (target == root.val) + \
                path_from(root.left, target - root.val) + \
                path_from(root.right, target - root.val)

        return path_from(root, targetNum) + \
            self.pathSum(root.left, targetNum) + \
            self.pathSum(root.right, targetNum)


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