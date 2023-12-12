from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]):
        if not root:
            return []

        res = 0

        def f_sum(n: Optional[TreeNode], sum_str: str):
            nonlocal res
            if not n:
                return

            sum_new = f'{sum_str}{n.val}'

            f_sum(n.left,  sum_new)
            f_sum(n.right, sum_new)

            if not n.left and not n.right:
                res += int(sum_new)

        f_sum(root, 0)
        return res


#       1
#      / \
#     2   3
tree = TreeNode(1, TreeNode(2), TreeNode(3))

#       4
#      / \
#     3   5
#    / \   \
#   1   2   6
tree1 = TreeNode(val=4,
                 left=TreeNode(val=3,
                               left=TreeNode(1),
                               right=TreeNode(2)),
                 right=TreeNode(val=5,
                                left=None,
                                right=TreeNode(6)))


sol = Solution()
print(sol.sumNumbers(tree))
