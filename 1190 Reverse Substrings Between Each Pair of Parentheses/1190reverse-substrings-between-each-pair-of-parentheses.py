class Solution:
    def reverseParentheses(self, s: str) -> str:
        n=len(s)
        l=[0]*n
        st=ans=[]
        d=1
        for i , ch in enumerate(s):
            if ch=='(':
                st.append(i)
            elif ch==')':
                j=st.pop()
                l[i]=j
                l[j]=i
        i=0
        while i<n:
            if s[i]>='a':
                ans.append(s[i])
            else:
                i=l[i]
                d=-d
            i+=d
        return ''.join(ans)

                