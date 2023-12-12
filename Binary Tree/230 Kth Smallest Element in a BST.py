from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if k == 1:
                return curr.val

            k -= 1
            curr = curr.right


#       4
#      / \
#     2   5
#    / \   \
#   1   3   6
tree1 = TreeNode(val=4,
                 left=TreeNode(val=2,
                               left=TreeNode(1),
                               right=TreeNode(3)),
                 right=TreeNode(val=5,
                                left=None,
                                right=TreeNode(6)))


sol = Solution()
print(sol.kthSmallest(tree1, 1))
