

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nNodes = 0
        newTail, tail = head, None
        while newTail:
            tail = newTail
            newTail = newTail.next
            nNodes += 1

        rot = k % nNodes
        if rot == 0:
            return head

        newTail = head
        steps = nNodes - rot - 1

        while newTail and steps > 0:
            newTail = newTail.next
            steps -= 1

        newHead = newTail.next
        newTail.next = None
        tail.next = head

        return newHead


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


sol = Solution().rotateRight(l, 4)
printList(sol)
