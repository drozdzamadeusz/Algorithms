from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 1:
            return True

        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[c].append(p)

        vis = set()

        def travel(c: int):
            if c in vis:
                return False
            
            if graph[c] == []:
                return True
                
            vis.add(c)
            for p in graph[c]:
                if not travel(p):
                    return False
            vis.remove(c)

            graph[c] = [] # No cycle for course
            return True

        for c in range(len(graph)):
            if not travel(c):
                return False
            
        return True

sol = Solution()
print(sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
