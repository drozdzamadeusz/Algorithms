from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def find_insect(head: ListNode) -> Optional[ListNode]:
    if not head:
        return

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow
    return


def find_first_insect(head: ListNode, insect: ListNode) -> Optional[ListNode]:
    if not head:
        return

    while head != insect:
        head = head.next
        insect = insect.next

    return head


########################################################################
#                    Cycle Detection in Linked List                    #
#  When both the slow and fast pointers meet at the same node,         #
#  it indicates the presence of a cycle in the list.                   #
########################################################################
#                                                                      #
#  1. Array representation of cycle                                    #
#     Value points to index in array                                   #
#                                                                      #
#   idx:    0     1     2     3     4                                  #
#                                                                      #
#                 ↙️───────────────↖️                                    #
#   val: [  1  ,  2  ,  3  ,  4  ,  1  ]                               #
#            ↘___↗ ↘____↗↘___↗↘____↗                                   #
#                                                                      #
#                 ↑                                                    #
#                 ⎩_  Multiple nodes point to a single node,           #
#                     proving that it is a cyclic list.                #
#                                                                      #
#                                                                      #
#   2. Linked List representation of a cycle:                          #
#                                                                      #
#                        (3)                                           #
#                       ↗️   ↘️                                          #
#      head:     (1) ➡️ (2)     〉                                      #
#                       ↖️   ↙️                                          #
#                     ↑  (4)                                           #
#                     |                                                #
#                     ⎩_ Multiple nodes point to a single node,        #
#                        proving that it is a cyclic list.             #
#                                                                      #
########################################################################


n2, n3, n4 = ListNode(2), ListNode(3), ListNode(4)
n2.next, n3.next, n4.next = n3, n4, n2
head1 = ListNode(1, n2)

head2 = ListNode(value=1, next=ListNode(value=2, next=ListNode(3)))

res = has_cycle(head2)
output = "No Cycle Detected" if not res else "Cycle Detected"
print(output)


insect = find_insect(head1)

res = find_first_insect(head1, insect)
print(res.value if res else "No first isect")
