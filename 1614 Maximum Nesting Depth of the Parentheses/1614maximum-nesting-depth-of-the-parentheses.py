class Solution:
    def maxDepth(self, s: str) -> int:
        ans=op=0
        for c in s:
            if c=="(":
                ans+=1
                op=max(ans,op)
            elif c==")":
                ans-=1
        return op
         
                     