class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            d=set()
            for j in range(i,n):
                d.add(nums[j])
                ans += len(d)* len(d)
        return ans 