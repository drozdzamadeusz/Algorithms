
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1, curr2 = headA, headB

        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA

        return curr1.val


l = ListNode(val=5)


sol = Solution()
print(
    sol.getIntersectionNode(
        ListNode(1, ListNode(2, l)),
        ListNode(6, ListNode(7))
    )
)
