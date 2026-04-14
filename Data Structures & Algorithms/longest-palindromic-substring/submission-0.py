class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start=0
        maxi=1
        dp=[[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                start=i
                maxi=2
        for length in range(3,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    if length>maxi:
                        maxi=length
                        start=i

        return s[start:maxi+start] 