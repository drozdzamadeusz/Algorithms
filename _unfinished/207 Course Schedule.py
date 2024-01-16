from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 1:
            return True

        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[p].append(c)

        vis = set()

        def travel(c: List):
            for p in c:
                if p in vis:
                    return False
                
                vis.add(p)
                if not travel(graph[p]):
                    return False
                vis.remove(p)

            return True

        # print(graph)

        for c in graph:
            vis.clear()
            if not travel(c):
                return False
            
        return True


sol = Solution()
print(sol.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
