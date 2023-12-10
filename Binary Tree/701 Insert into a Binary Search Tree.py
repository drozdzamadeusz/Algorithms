from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root, level=0, prefix="R:  "):
    if root is not None:
        print(" " * (4 * level) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree(root.left, level + 1, "L-- ")
            else:
                print(" " * (4 * (level + 1)) + "L-- None")
            if root.right:
                print_tree(root.right, level + 1, "R-- ")
            else:
                print(" " * (4 * (level + 1)) + "R-- None")



class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root


#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                 TreeNode(5, right=TreeNode(6)))


#       1
tree2 = TreeNode(1)


#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))


sol = Solution()
print(print_tree(sol.insertIntoBST(tree1, 7)))
