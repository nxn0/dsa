class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9+7
        n = len(arr)
        dp = [[0,0],[0,0]]
        ans =dp[1][0]
        for i in range(n):
            idx = i&1
            p = arr[i] & 1
            dp[p][idx] = (1 + dp[0][1 - idx]) % mod
            dp[1 - p][idx] = dp[1][1 - idx] % mod
            ans = (ans+dp[1][idx])%mod
       
        return ans

        
