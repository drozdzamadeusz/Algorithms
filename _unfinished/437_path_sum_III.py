from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def pathSum(node: Optional[TreeNode], target: int, path: []):
            if not node:
                return

            if node.val == target:
                res.append(path + [node.val])

            pathSum(node.left, target - node.val, path + [node.val])
            pathSum(node.right, target - node.val, path + [node.val])

        pathSum(root, targetSum, [])
        return res


#       2
#      / \
#     2   2
#    / \   \
#   17  4   2
#          /
#         8
tree1 = TreeNode(2, TreeNode(2, TreeNode(17), TreeNode(4)),
                 TreeNode(2, TreeNode(2, TreeNode(8))))


sol = Solution()
print(sol.pathSum(tree1, 6))
