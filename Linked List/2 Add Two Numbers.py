from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        curr = ListNode(0)
        res = curr

        while l1 or l2 or carry:
            l1V, l2V = l1.val if l1 else 0, l2.val if l2 else 0
            sum = (l1V + l2V + carry) % 10
            carry = (l1V + l2V + carry) // 10

            curr.next = ListNode(sum)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return res.next


sol = Solution()
print(sol.addTwoNumbers(l1=ListNode(2, ListNode(4)),
                        l2=ListNode(5, ListNode(6, ListNode(4)))))
