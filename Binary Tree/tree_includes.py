from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## Iterative method (Breadth first search)
# class Solution:
#    def treeIncludes(self, root: Optional[TreeNode], target: int):
#        if not root:
#            return False

#        queue = [root]

#        while len(queue) > 0:
#            curr = queue.pop(0)

#            if curr.val == target: 
#                return True

#            if curr.left:
#                queue.append(curr.left)

#            if curr.right:
#                queue.append(curr.right)

#        return False


# Recursive method:
class Solution:
    def treeIncludes(self, root: Optional[TreeNode], target: int):
        if not root:
            return False
        
        if root.val == target:
            return True

        left = self.treeIncludes(root.left, target)
        right = self.treeIncludes(root.right, target)

        return left or right

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
print(sol.treeIncludes(tree1, 1))
