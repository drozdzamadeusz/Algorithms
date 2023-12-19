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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lSideTail, revTail = None, None
        c, p = head, None
        index = 0

        while c:
            tmp = c.next
            index += 1

            if left > index:
                lSideTail = c  # Preserve last non-swapped node
                c = tmp
                continue
            if right < index:
                break

            c.next, p = p, c  # Swap nodes

            if left == index:  # Preserve tail of rev nodes
                revTail = c

            if right == index:
                revTail.next = tmp

                if not lSideTail:
                    return c

                lSideTail.next = c
                return head

            c = tmp

        return head


l = ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=4,
                                                       next=ListNode(5)))))


l1 = ListNode(val=3,
              next=ListNode(val=5))

l3 = ListNode(5)


sol = Solution()
res = sol.reverseBetween(l, 2, 4)
printList(res)


res = sol.reverseBetween(l1, 1, 1)
printList(res)

res = sol.reverseBetween(l3, 1, 1)
printList(res)
