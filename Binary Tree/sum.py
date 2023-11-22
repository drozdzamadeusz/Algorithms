from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method:
# class Solution:
#     def treeSum(self, root: Optional[TreeNode]):
#         if not root:
#             return 0

#         left = self.treeSum(root.left)
#         right = self.treeSum(root.right)

#         return root.val + left + right


# Iterative method
class Solution:
    def treeSum(self, root: Optional[TreeNode]):
        if not root:
            return 0

        sum = 0
        queue = [root]

        while len(queue) > 0:
            curr = queue.pop(0)

            sum += curr.val

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return sum

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
print(sol.treeSum(tree1))
