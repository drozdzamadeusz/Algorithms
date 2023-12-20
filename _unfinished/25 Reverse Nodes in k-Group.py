from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        


l = ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=4,
                                                       next=ListNode(val=5)))))


def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


sol = Solution()
res = sol.deleteDuplicates(l)
printList(res)
