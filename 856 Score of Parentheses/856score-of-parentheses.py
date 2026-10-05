class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #(a) has q score 2 x a I'll look it later
        ans =0
        st=[0]
        for c in s:
            if c=='(':
                st.append(0)
                
            else:
                ans= st.pop()
                st[-1]+= max(1,ans*2)
                
        return st[-1]
           