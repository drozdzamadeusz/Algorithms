
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMid(head: ListNode) -> ListNode:
            prev = None
            slow, fast = head, head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            return slow

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        mid = findMid(head)
        root = TreeNode(mid.val)
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root


l = ListNode(val=-10,
             next=ListNode(val=-3,
                           next=ListNode(val=0,
                                         next=ListNode(val=5,
                                                       next=ListNode(9)))))

l2 = ListNode(val=-10,
              next=ListNode(val=0,
                            next=ListNode(val=3, next=ListNode(5))))

l3 = ListNode(val=1,
              next=ListNode(val=2,
                            next=ListNode(val=3)))


sol = Solution()
print(sol.sortedListToBST(l))
