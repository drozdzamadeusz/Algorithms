from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def travel(node: TreeNode):
             if not node:
                return chr(255)
              
             if not node.left and not node.right:
                 return chr(node.val + 97)

             left = travel(node.left)
             right = travel(node.right)

             smaller = min(left, right)

             return smaller + chr(node.val + 97)


        return travel(root)


sol = Solution()
a = sol.smallestFromLeaf(TreeNode(
    val=25,
    left=TreeNode(val=1, left=TreeNode(1), right=TreeNode(3)),
    right=TreeNode(val=3, left=TreeNode(0), right=TreeNode(2))))
print(a)