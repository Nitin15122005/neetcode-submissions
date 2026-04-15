class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        n=len(nums)
        visited=[False]*n
        def backtrack():
            if len(sub)==n: res.append(sub[:])
            for i in range(n):
                if visited[i]==True: continue
                visited[i]=True
                sub.append(nums[i])
                backtrack()
                sub.pop()
                visited[i]=False
        backtrack()
        return res