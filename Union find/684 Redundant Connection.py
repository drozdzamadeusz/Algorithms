from typing import List

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         graph = [[] for _ in range(len(edges) + 1)]

#         for u, v in edges:
#             graph[v].append(u)
#             graph[u].append(v)

#         def travel(u: int):
#             q = Deque([u])
#             vis = set()

#             while q:
#                 curr = q.popleft()

#                 for v in graph[curr]:
#                     if v in vis:
#                         return [curr, v]

#                     vis.add(v)
#                     q.append(v)


#         for u in range(1, len(graph)):
#             t = travel(u)
#             if t:
#                 return t


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


sol = Solution()
print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
