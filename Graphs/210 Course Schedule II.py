from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[c].append(p)

        vis = set()
        order = []

        def dfs(c: int):
            if c in vis:
                return False

            if graph[c] == [] and c in order:
                return True

            vis.add(c)
            for p in graph[c]:
                if not dfs(p):
                    return False
            vis.remove(c)

            graph[c] = []
            order.append(c)

            return True

        for c in range(len(graph)):
            if not dfs(c):
                return []

        return order


sol = Solution()
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
