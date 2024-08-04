from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return 1
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        res = []
        longest = 0

        for g in graph:
            n = graph[g]
            longest = max(longest, len(n))

        for g in graph:
            n = graph[g]
            if len(n) == longest:
                res.append(g)
        
sol = Solution()
# print(sol.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
# print(sol.findMinHeightTrees(n=6, edges=[
#       [3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))

print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]

))
