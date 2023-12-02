from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []

        def dfsPath(node: Optional[TreeNode], path):
            if not node:
                return

            newPath = path + '->' + str(node.val) if path else str(node.val)

            if not node.left and not node.right:
                res.append(newPath)
                return

            dfsPath(node.left, newPath)
            dfsPath(node.right, newPath)

        dfsPath(root, [])
        return res


#       1
#      / \
#     2   5
#    / \   \
#   17  4   6
#          /
#         8
tree1 = TreeNode(1, TreeNode(2, TreeNode(17), TreeNode(4)),
                 TreeNode(5, TreeNode(6, TreeNode(8))))


#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))


sol = Solution()
print(sol.binaryTreePaths(tree1))
