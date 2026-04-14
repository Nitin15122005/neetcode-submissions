class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1: return nums[0]
        def rob_linear(arr):
            n=len(arr)
            if n == 1: return arr[0]
            rob=[0]*(n)
            rob[0]=arr[0]
            rob[1]=max(arr[0],arr[1])
            for i in range(2,n):
                rob[i]=max(rob[i-1],arr[i]+rob[i-2])

            return rob[-1]

        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))