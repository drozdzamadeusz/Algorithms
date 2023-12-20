from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c, d = head, ListNode()
        dH = d

        while c:
            dist = True

            while c.next and c.val == c.next.val:
                dist = False
                c = c.next

            if dist:
                d.next = c
                d = d.next

            c = c.next

        d.next = None

        return dH.next


l = ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=3,
                                                       next=ListNode(val=4,
                                                                     next=ListNode(val=4,
                                                                                   next=ListNode(5)))))))

l1 = ListNode(val=1,
              next=ListNode(val=2,
                            next=ListNode(val=2)))


def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


sol = Solution()

res = sol.deleteDuplicates(l)
printList(res)
