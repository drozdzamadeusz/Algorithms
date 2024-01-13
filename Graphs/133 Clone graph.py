from typing import Deque, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        q = Deque([node])

        clone = {}
        clone[node] = Node(node.val) # Add root to clone

        while q:
            curr = q.popleft()

            for n in curr.neighbors:

                if n not in clone:
                    clone[n] = Node(n.val)
                    q.append(n)

                clone[curr].neighbors.append(clone[n]) 

        return clone[node]


graph1 = Node(1)
graph2 = Node(2)
graph3 = Node(3)
graph4 = Node(4)

graph1.neighbors = [graph2, graph4]
graph2.neighbors = [graph1, graph3]
graph3.neighbors = [graph2, graph4]
graph4.neighbors = [graph1, graph3]

sol = Solution()
print(sol.cloneGraph(graph1))
