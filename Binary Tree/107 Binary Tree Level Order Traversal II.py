from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         res = []
#         q = [root]

#         while len(q):
#             levNodes = []
#             levLen = len(q)

#             for i in range(levLen):

#                 curr = q.pop(0)
#                 levNodes.append(curr.val)

#                 if curr.left:
#                     q.append(curr.left)

#                 if curr.right:
#                     q.append(curr.right)

#             res.append(levNodes)

#         return res[::-1]


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while len(q):
            levNodes = []
            levLen = len(q)

            for _ in range(levLen):

                curr = q.pop(0)
                levNodes.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            res.insert(0, levNodes)

        return res

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
print(sol.levelOrderBottom(tree1))
