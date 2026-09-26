class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        mx = 0
        n = len(nums)

        for i in range(n):
            curr = 0
            we = set()
            for j in range(i,n):
                curr +=nums[j]
                we.add((2*nums[j])%k)
                if curr%k==0:
                    mx=max(mx,j-i+1)
                elif(curr%k) in we:
                    mx = max(mx,j-i+1)      
        return mx
        