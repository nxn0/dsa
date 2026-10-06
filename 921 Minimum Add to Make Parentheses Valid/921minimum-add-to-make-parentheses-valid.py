class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=0
        ans=0
        for c in s:
            if c == '(':
                a+=1
            else:
                a-=1
                if a<0:
                    ans+=1
                    a=0
        return ans +a