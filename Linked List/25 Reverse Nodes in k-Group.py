from typing import Deque, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head

        # Helpers
        def isH(i): return i % k == 0  # True if N is the head of a gr.
        def isT(i): return i % k == k - 1  # True if N is the tail of a gr.
        def isS(i): return i + 1 == k  # True if N is the start of the list.

        # Used for storing the head and tail of the group.
        q = Deque([], maxlen=2)

        c, p, i = head, None, 0
        while c:
            if isH(i):
                q.append(c)  # Store group head
                p = None
            elif isS(i):
                head = c  # Start of the list: set head to current N
            elif isT(i):
                q.popleft().next = c  # Link the group head to current N

            # Reverse
            tmp = c.next
            p, c.next = c, p
            c = tmp

            i += 1

        f = q.popleft()
        l = q.popleft() if q else None

        if not l:
            return head

        f.next = l

        c, p = p, None
        while c:
            tmp = c.next
            p, c.next = c, p
            c = tmp

        return head


def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


l = ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=4,
                                                       next=ListNode(5)))))

sol = Solution().reverseKGroup(l, 3)
printList(sol)
