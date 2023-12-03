from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]):
#         if not root:
#             return []

#         res = []
#         stack = [root]

#         while len(stack) > 0:
#             curr = stack.pop()
#             res.append(curr.val)

#             if curr.left:
#                 stack.append(curr.left)

#             if curr.right:
#                 stack.append(curr.right)

#         return res[::-1]

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return []
        

        l = self.postorderTraversal(root.left)
        r = self.postorderTraversal(root.right)

        return l + r + [root.val]


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
print(sol.postorderTraversal(tree1))
