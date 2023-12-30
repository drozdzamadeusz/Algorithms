from typing import Optional
import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:
            l1V = s1.pop() if s1 else 0
            l2V = s2.pop() if s2 else 0

            sum = (l1V + l2V + carry) % 10
            carry = (l1V + l2V + carry) // 10

            node = ListNode(sum)
            node.next = head
            head = node

        return head


sol = Solution()
res = sol.addTwoNumbers(l1=ListNode(7, ListNode(2, ListNode(4, ListNode(3)))),
                        l2=ListNode(5, ListNode(6, ListNode(4))))

# while res:
#     print(res.val, end=" ")
#     res = res.next

print(json.dumps(res))
