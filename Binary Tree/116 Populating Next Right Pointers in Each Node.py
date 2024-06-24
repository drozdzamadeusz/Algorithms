
# Definition for a Node.
from typing import Deque, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return

        q = Deque([(root, 0)])

        prev, prev_lv = None, -1

        while q:
            curr, curr_lv = q.popleft()

            if prev_lv != curr_lv:
                prev = None

            if prev:
                prev.next = curr

            if curr.left:
                q.append((curr.left, curr_lv + 1))

            if curr.right:
                q.append((curr.right, curr_lv + 1))

            prev, prev_lv = curr, curr_lv

        return root


t = Node(val=1,
         left=Node(
             val=2,
             left=Node(4),
             right=Node(5)
         ),
         right=Node(
             val=3,
             left=Node(6),
             right=Node(7)
         )
         )


sol = Solution()
print(sol.connect(t))
