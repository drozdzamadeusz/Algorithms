from typing import Deque, List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]

        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        def travel(u: int):
            q = Deque([u])
            vis = set()

            while q:
                curr = q.pop()

                for v in graph[curr]:
                    if v in vis:
                        return [curr, v]

                    vis.add(v)
                    q.append(v)


        for u in range(1, len(graph)):
            t = travel(u)
            if t:
                return t



sol = Solution()
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
