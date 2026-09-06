class Solution:
    def countRotations(self, s: str, k: int) -> int:
        conc = s + s
        n = len(s)
        ans = 0
        
        for i in range (n):
            r = conc[i: i+n]
            matcnt = sum(a == b for a, b in zip(r, r[1:]))
            if matcnt == k:
                ans += 1
        return ans
            
            