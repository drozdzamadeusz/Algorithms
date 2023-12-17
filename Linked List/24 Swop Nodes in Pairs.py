
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        resPtr = head.next
        c, prev = head, None

        while c:
            tmp = c.next
            
            # If prev is None, set prev to current and move forward
            if not prev:
                c, prev = tmp, c
                continue

            # Set current pointer next ref
            c.next = prev

            # Set previous pointer next ref
            if tmp and tmp.next:
                prev.next = tmp.next
            else:
                prev.next = tmp
                break

            # Move forward and set prev to None
            c, prev = tmp, None

        return resPtr


def printList(head: ListNode):
    i = 0
    while head and i < 4:
        print(head.val, end=" ")
        head = head.next
        i += 1
    print()


l = ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=4))))

sol = Solution().swapPairs(l)
printList(sol)
