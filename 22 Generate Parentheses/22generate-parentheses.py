class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return (f:=lambda p,l,r:l==r==n and [p] or r<=l<=n and f(p+'(', l+1,r)+f(p+')',l,r+1) or [])('',0,0)