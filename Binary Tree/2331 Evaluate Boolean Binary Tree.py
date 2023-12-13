from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val <= 1:
            return True if root.val == 1 else False
        
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        

        


tree1 = TreeNode(val=2,
                 left=TreeNode(val=1),
                 right=TreeNode(val=3,
                                left=TreeNode(0),
                                right=TreeNode(1)))




sol = Solution()
print(sol.evaluateTree(tree1))
