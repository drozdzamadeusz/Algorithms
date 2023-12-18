from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def path_sum(node: Optional[TreeNode], path: [], target: int):
            nonlocal res
            if not node:
                return None
            
            newPath = []
            newTarget = targetSum
            if node.val == target:
                res += 1

            elif node.val > target:
                newTarget = targetSum
                newPath = []

            else:
                newPath = path + [node.val]
                newTarget = target - node.val


            path_sum(node.left, newPath, newTarget)
            path_sum(node.right, newPath, newTarget)

        path_sum(root, [], targetSum)
        return res
    


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