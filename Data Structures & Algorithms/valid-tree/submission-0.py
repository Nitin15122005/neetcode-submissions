class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(parent,x):
            if parent[x]!=x: 
                parent[x]=find(parent,parent[x])
            return parent[x]

        def union(u,v):
            pu=find(parent,u)
            pv=find(parent,v)
            if pu==pv: return True
            parent[pu]=pv
            return False

        if len(edges) != n - 1: return False
        parent=[i for i in range(n)]

        for u,v in edges:
            ans=union(u,v)
            if ans: return False
        return True