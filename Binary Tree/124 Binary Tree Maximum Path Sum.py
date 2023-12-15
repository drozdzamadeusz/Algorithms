import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPath(root: Optional[TreeNode], maxEnded: int):

            if not root:
                return [0, maxEnded]

            if root.val and not root.left and not root.right:
                return [root.val, max(maxEnded, root.val)]

            lNode = maxPath(root.left, maxEnded)
            rNode = maxPath(root.right, maxEnded)

            lVal, rVal = max(0, lNode[0]), max(0, rNode[0])
            lMax, rVal = lNode[1], rNode[1]

            path = root.val + max(lVal, rVal)
            newMaxEnded = max(lMax, rVal, root.val + lVal + rVal)

            return [path, newMaxEnded]

        return maxPath(root, -math.inf)[1]
    




tree = TreeNode(val=1,
                left=TreeNode(val=2,
                              left=TreeNode(val=8,
                                            left=TreeNode(4),
                                            right=TreeNode(6)),
                              right=TreeNode(10)),
                right=TreeNode(3))


tree2 = TreeNode(val=1,
                 left=TreeNode(val=4,
                               left=TreeNode(val=-10,
                                             left=TreeNode(val=-4,
                                                           left=TreeNode(-15),
                                                           right=TreeNode(20),
                                                           ),
                                             right=TreeNode(val=-7,
                                                            left=TreeNode(1),
                                                            right=TreeNode(19)
                                                            ),
                                             )
                               ),
                 right=TreeNode(val=1,
                                left=TreeNode(-100),
                                right=TreeNode(99)
                                )
                 )


#       3
#      / \
#     1   4
tree3 = TreeNode(val=3,
                 left=TreeNode(val=1),
                 right=TreeNode(val=4))


tree4 = TreeNode(val=2,
                 left=None,
                 right=TreeNode(val=4,
                                left=TreeNode(10),
                                right=TreeNode(val=8,
                                               left=TreeNode(4),
                                               right=None)))


sol = Solution()
print(sol.maxPathSum(tree))
