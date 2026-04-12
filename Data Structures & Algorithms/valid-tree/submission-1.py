class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {node:[] for node in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited: 
                    if dfs(neighbour,node): return True
                elif neighbour!=parent: return True
            return False

        if dfs(0, -1):
            return False

        return len(visited) == n