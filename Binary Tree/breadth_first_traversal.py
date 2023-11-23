from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def breadthFirstTraversal(self, root: Optional[TreeNode]):
        if not root:
            return []

        res = []
        queue = [root]

        while len(queue) > 0:
            curr = queue.pop(0)

            res.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return res

# Recursive method -> Needs a queue, so it's not worth implementing a recursive method. I'd be really difficult to have correct order.


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
print(sol.breadthFirstTraversal(tree1))
