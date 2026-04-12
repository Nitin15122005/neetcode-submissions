class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {node:[] for node in range(numCourses)}

        for u, v in prerequisites:
            graph[v].append(u)

        visited = set()
        rec_stack=set()
        def dfs(node):
            if node in rec_stack: return True
            if node in visited: return False
            visited.add(node)
            rec_stack.add(node)
            for neighbour in graph[node]: 
                if dfs(neighbour): return True
            rec_stack.remove(node)
            return False

        for courses in range(numCourses):
            if courses not in visited:
                if dfs(courses):
                    return False

        return True