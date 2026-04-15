class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        n=len(candidates)
        candidates.sort()
        def backtrack(start,current_sum):
            if current_sum==target : res.append(subset[:])
            if current_sum<target:
                for i in range(start,n):
                    if i>start and candidates[i]==candidates[i-1]: continue 
                    current_sum+=candidates[i]
                    subset.append(candidates[i])
                    backtrack(i+1,current_sum)
                    current_sum-=candidates[i]
                    subset.pop()
        backtrack(0,0)
        return res