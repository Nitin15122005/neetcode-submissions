class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        n=len(nums)
        def backtrack(start,current_sum):
            if current_sum==target: res.append(subset[:])
            if current_sum<target:
                for i in range(start,n):
                    current_sum+=nums[i]
                    subset.append(nums[i])
                    backtrack(i,current_sum)
                    current_sum-=nums[i]
                    subset.pop()
        backtrack(0,0)
        return res