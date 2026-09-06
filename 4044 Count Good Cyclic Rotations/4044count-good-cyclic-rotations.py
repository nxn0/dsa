class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        conc = nums + nums
        ans  = 0
        n = len(nums)
        half = n//2
        pre = [0] * (2 * n+1)
        for i in range (2*n):
            pre[i+1] = pre[i] + conc[i]
        for i in range(n):
            a = pre[i + half] - pre[i]
            b = pre[i + n] - pre[i+ half]
            if a > b:
                ans +=1
        return ans