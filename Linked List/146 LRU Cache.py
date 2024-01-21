class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Left, Front -> LRU
        # Right End -> MRU
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert_right(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        cache = self.cache
        if key not in cache:
            return -1

        node = cache[key]
        self.remove(node)
        self.insert_right(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        if key in cache:
            node = cache[key]
            node.val = value
            self.remove(node)
            self.insert_right(node)
        else:
            if len(cache) >= self.capacity:
                lru = self.left.next
                self.remove(lru)
                del cache[lru.key]

            cache[key] = Node(key, value)
            self.insert_right(cache[key])


# Your LRUCache object will be instantiated and called as such:
sol = LRUCache(1)
sol.put(2, 1)
sol.get(2)
