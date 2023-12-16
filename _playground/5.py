class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move slow pointer one step
        fast = fast.next.next     # move fast pointer two steps

        if slow == fast:          # cycle detected
            return True

    return False

# Example usage
# Create a linked list with a cycle for demonstration
# Node 1 -> Node 2 -> Node 3 -> Node 4 -> Node 2 (cycle)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)


#           (3)
#          ↗️   ↘️
# (1) ➡️ (2)     〉 
#          ↖️   ↙️
#           (4)   

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print("Cycle Detected:" if has_cycle(node1) else "No Cycle Detected")