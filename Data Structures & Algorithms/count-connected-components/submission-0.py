class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(parent,x):
            if parent[x]!=x: parent[x]=find(parent,parent[x])
            return parent[x]

        def union(u,v):
            pu,pv=find(parent,u),find(parent,v)
            if pu==pv: return 0
            parent[pv]=pu
            return -1

        province=n
        parent=[i for i in range(n)]
        for u,v in edges:
            province+=union(u,v)
        return province