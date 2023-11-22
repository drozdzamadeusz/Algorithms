from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []

        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)

            curr = curr.right

        return res


#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(5, TreeNode(6)))


#       1
tree2 = TreeNode(1)


#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))


sol = Solution()
print(sol.inorderTraversal(tree3))
