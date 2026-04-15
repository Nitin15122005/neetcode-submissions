class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sub=[]
        n=len(s)
        def is_palindrome(left,right):
                while left<=right:
                        if s[left]!=s[right]: return False
                        left+=1 
                        right-=1
                return True
        def backtrack(start):
                if start==n: res.append(sub[:])
                for end in range(start,n):
                        if is_palindrome(start,end):
                                sub.append(s[start:end+1])
                                backtrack(end+1)
                                sub.pop()
        backtrack(0)
        return res