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
    

# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
        
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



#       4
#      / \
#     2   5
#    / \   \
#   1   3   6
tree1 = TreeNode(val=4,
                 left=TreeNode(val=3,
                               left=TreeNode(1),
                               right=TreeNode(3)),
                 right=TreeNode(val=5,
                                left=None,
                                right=TreeNode(6)))




sol = Solution()
print(sol.inorderTraversal(tree1))
