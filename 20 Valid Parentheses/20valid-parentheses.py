class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        p = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in p.keys():
                st.append(c)
            elif c in p.values():
                if not st or p[st.pop()] != c:
                    return False
        return not st


          
       
