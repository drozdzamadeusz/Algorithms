from typing import Deque, Dict, List


def dfs(graph: Dict[str, List[str]], res: str, dst: str) -> bool:
    if res == dst:
        return True

    for n in graph[res]:
        if dfs(graph, n, dst):
            return True
    return False


def bfs(graph: Dict[str, List[str]], res: str, dst: str) -> bool:
    q = Deque(res)
    vis = set()

    while q:
        curr = q.popleft()

        if curr == dst:
            return True

        for n in graph[curr]:
            if n in vis:
                continue
            q.append(n)
            vis.add(n)
    return False



#       (A)
#      ↙️  ↘️
#    (B)  (C)
#      ↘️  ↙️
#       (D)
#        ↓
#       (E)
graph = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": ["d"]}
print(bfs(graph, "a", "e"))
