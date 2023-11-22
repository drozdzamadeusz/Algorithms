from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Iterative method:
# class Solution:
#     def depthFirstTraversal(self, root: Optional[TreeNode]):
#         if not root:
#             return []

#         res = []
#         stack = [root]


#         while len(stack) > 0:
#             curr = stack.pop()

#             res.append(curr.val)

#             if curr.right:
#                 stack.append(curr.right)

#             if curr.left:
#                 stack.append(curr.left)

#         return res



# Recursive method:
class Solution:
    def depthFirstTraversal(self, root: Optional[TreeNode]):
        if not root:
            return []

        leftVals = self.depthFirstTraversal(root.left)
        rightVals = self.depthFirstTraversal(root.right)

        return [root.val] + leftVals + rightVals

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
print(sol.depthFirstTraversal(tree1))
