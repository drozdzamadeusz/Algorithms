from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return []

        res = []
        stack = [(root, False)]

        while len(stack) > 0:
            curr, visited = stack.pop()

            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))


        return res

# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]):
#         if not root:
#             return []
        

#         l = self.postorderTraversal(root.left)
#         r = self.postorderTraversal(root.right)

#         return l + r + [root.val]


#       6
#      / \
#     3   5
#    / \   \
#   1   2   4
tree1 = TreeNode(val=6,
                 left=TreeNode(val=3,
                               left=TreeNode(1),
                               right=TreeNode(2)),
                 right=TreeNode(val=5,
                                left=None,
                                right=TreeNode(4)))

sol = Solution()
print(sol.postorderTraversal(tree1))
