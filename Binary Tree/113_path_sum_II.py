from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def dfsPaths(root: Optional[TreeNode], target: int, path):
            if not root:
                return

            if target == root.val and not root.left and not root.right:
                res.append(path + [root.val])
                return

            dfsPaths(root.left, target - root.val, path + [root.val])
            dfsPaths(root.right, target - root.val, path + [root.val])

        dfsPaths(root, targetSum, [])

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


sol = Solution()
print(sol.pathSum(tree1, 20))
