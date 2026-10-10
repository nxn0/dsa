class Solution:
    def reverseVowels(self, s: str) -> str:
        ar = []
        t=0
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                ar.append(c)
        
                #t is the index of indarr, and i is the actual index in actual string stored in indarr
        ar = ar[::-1]
        s=list(s)
        for i,c in enumerate(s):
            if c in 'aeiouAEIOU' :
                s[i]=ar[t]
                t+=1
        return ''.join(s)
        
        