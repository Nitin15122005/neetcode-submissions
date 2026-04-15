class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        sub=[]
        def backtrack(start,current_sum):
                res.append(sub[:])
                for i in range(start,n):
                    if i>start and nums[i]==nums[i-1]: continue
                    current_sum+=nums[i]
                    sub.append(nums[i])
                    backtrack(i+1,current_sum)
                    sub.pop()
                    current_sum-=nums[i]
        backtrack(0,0)
        return res