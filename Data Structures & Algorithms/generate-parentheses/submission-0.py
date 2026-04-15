class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(s,open,close):
                if len(s)==2*n: res.append(s)
                else:
                        if open<n:
                                open+=1
                                s=s+"("
                                backtrack(s,open,close)
                                open-=1
                                s=s[:-1]
                        if close<open:
                                close+=1
                                s=s+")"
                                backtrack(s,open,close)
                                close-=1
                                s=s[:-1]
        backtrack("",0,0)
        return res