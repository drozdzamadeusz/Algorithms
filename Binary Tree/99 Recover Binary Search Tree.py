from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []
        curr = root

        f, s, prev = None, None, None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            print(curr.val)

            if prev:
                if prev.val > curr.val and not f:
                    f = prev

                if prev.val > curr.val and f:
                    s = curr

            prev = curr
            curr = curr.right

        f.val, s.val = f.val, s.val

        return root


#       4
#      / \
#     5   2
#    / \   \
#   1   3   6
tree1 = TreeNode(val=4,
                 left=TreeNode(val=5,
                               left=TreeNode(1),
                               right=TreeNode(3)),
                 right=TreeNode(val=2,
                                left=None,
                                right=TreeNode(6)))


sol = Solution()
print(sol.recoverTree(tree1))
