from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot

        def sameTree(s: Optional[TreeNode], t: Optional[TreeNode]):
            if not s or not t:
                return s == t

            return s.val == t.val and \
                sameTree(s.left, t.left) and \
                sameTree(s.right, t.right)

        return sameTree(root, subRoot) or \
            self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)


#       3
#      / \
#     4   5
#        / \
#       6   7
tree2 = TreeNode(3, left=TreeNode(9), right=TreeNode(
    5, left=TreeNode(6), right=TreeNode(7)))

#      5
#     / \
#    6   7
tree3 = TreeNode(5, left=TreeNode(6), right=TreeNode(7))


sol = Solution()
print(sol.isSubtree(tree2, tree2))
