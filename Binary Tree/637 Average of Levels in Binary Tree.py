from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        quere = [root]

        while len(quere):
            avg = 0
            nLevel = len(quere)

            for i in range(nLevel):
                curr = quere.pop(0)
                avg += curr.val

                print(curr.val)

                if curr.left:
                    quere.append(curr.left)

                if curr.right:
                    quere.append(curr.right)

            avg /= nLevel
            res.append(avg)

        return res


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
print(sol.averageOfLevels(tree1))
