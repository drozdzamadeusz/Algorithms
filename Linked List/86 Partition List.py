
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        g = ListNode()
        greaterHead, lessHead = g, head

        c, prev = head, None

        while c:
            if c.val < x:
                prev = c
                c = c.next
                continue

            g.next = c
            g = g.next

            if not prev:
                lessHead = c.next
            else:
                prev.next = c.next

            c = c.next

        g.next = None

        if prev:
            prev.next = greaterHead.next
        else:
            lessHead = greaterHead.next

        return lessHead


l = ListNode(val=1,
             next=ListNode(val=4,
                           next=ListNode(val=3,
                                         next=ListNode(val=2,
                                                       next=ListNode(val=5,
                                                                     next=ListNode(2))))))
l1 = ListNode(val=1,
              next=ListNode(val=1))


def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


sol = Solution().partition(l1, 0)
printList(sol)
