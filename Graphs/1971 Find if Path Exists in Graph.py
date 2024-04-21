from typing import Deque, List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        graph = {i: [] for i in range(n)}

        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)

        q = Deque(graph[source])
        vis = set(q)

        while q:
            curr = q.popleft()
            if curr == destination:
                return True

            for n in graph[curr]:
                if n not in vis:
                    q.append(n)
                    vis.add(n)

        return False


sol = Solution()
print(sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
