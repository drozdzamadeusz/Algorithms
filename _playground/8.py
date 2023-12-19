
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l = ListNode(val=1,
             next=ListNode(val=2,
                           next=ListNode(val=3,
                                         next=ListNode(val=4,
                                                       next=ListNode(5)))))


c, p = l, None

while c:
    tmp = c.next
    c.next = p
    p = c
    c = tmp


def printList(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


printList(p)
