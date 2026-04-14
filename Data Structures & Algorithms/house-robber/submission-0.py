class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]

        rob=[0]*(n)
        rob[0]=nums[0]
        rob[1]=max(nums[0],nums[1])
        for i in range(2,n):
            rob[i]=max(rob[i-1],nums[i]+rob[i-2])

        return rob[-1]

        return max(rob)