import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> bool:

#         def max_sum_path(node: Optional[TreeNode], max_sum: Optional[int], sum_path: Optional[int]):
#             if not node:
#                 return max_sum

#             if not max_sum:
#                 max_sum = node.val
#                 sum_path = node.val
#             else:
#                 sum_path += node.val

#                 if sum_path > max_sum:
#                     max_sum = sum_path

#             maxL = max_sum_path(node.left, max_sum, sum_path)
#             maxR = max_sum_path(node.right, max_sum, sum_path)

#             return max(maxL, maxR)

#         return root.val + max_sum_path(root.left, None, None) + max_sum_path(root.right, None, None)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -math.inf

        def maxPathSumDownFrom(root: Optional[TreeNode]) -> int:
            nonlocal ans

            if not root:
                return 0

            l = max(0, maxPathSumDownFrom(root.left))
            r = max(0, maxPathSumDownFrom(root.right))

            ans = max(ans, root.val + l + r)
            
            return root.val + max(l, r)

        maxPathSumDownFrom(root)
        return ans



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
tree1 = TreeNode(val=3,
                 left=TreeNode(val=1),
                 right=TreeNode(val=4))


tree3 = TreeNode(val=2,
                 left=None,
                 right=TreeNode(val=4,
                                left=TreeNode(10),
                                right=TreeNode(val=8,
                                               left=TreeNode(4),
                                               right=None)))


sol = Solution()
print(sol.maxPathSum(tree2))
