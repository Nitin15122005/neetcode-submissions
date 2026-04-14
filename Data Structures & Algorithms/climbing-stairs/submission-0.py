class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1: return 1
        dp=[-1]*(n+1)
        def climb(n):
            if dp[n]!=-1: return dp[n]
            if n==1 or n==0: 
                dp[n]=1
                return 1
            dp[n]=climb(n-1)+climb(n-2)
            return dp[n]
        climb(n)
        return dp[n]