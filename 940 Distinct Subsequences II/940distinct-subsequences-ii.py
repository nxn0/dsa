class Solution:
    
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 +7
        t= 0
        dp = [0]*26

        for c in s:
            c= ord(c) - 97
            new = t+1-dp[c]
            t = (t+new) % mod
            dp[c] = (dp[c] + new) % mod
        return t