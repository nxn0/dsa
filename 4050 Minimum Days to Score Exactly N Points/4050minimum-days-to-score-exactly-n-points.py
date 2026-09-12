class Solution:
    def minDays(self, n: int) -> int:
        tri = []
        k = 1
        while k * (k+1) // 2 <= n:
            tri.append((k*(k+1)//2,k))
            k+=1
        dp = [float('inf')] * (n+1)
        for val, d in tri:
            dp[val] = d
        for s in range(1,n+1):
            if dp[s]== float('inf'):
                continue
            c = dp[s]
            for val, d in tri:
                if s+val > n:
                    break
                if c + d+1 < dp[s+val]:
                    dp[s+val] = c +d+1
        return dp[n]
                
                
            
            

        
        
        
        