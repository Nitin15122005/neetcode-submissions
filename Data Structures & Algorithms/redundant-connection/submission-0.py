class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def find(parent,x):
            if parent[x]!=x:
                parent[x]=find(parent,parent[x])
            return parent[x]

        parent=[i for i in range(len(edges)+1)]

        def union(x,y):
            px=find(parent,x)
            py=find(parent,y)

            if py==px:
                return [x,y]
            
            parent[px]=py
            return None

        for i in edges:
            ans=union(i[0],i[1])
            if ans: return ans
