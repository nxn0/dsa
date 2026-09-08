class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        curr = 0
        for i in range(n):
            if nums[i] == 1:
                curr +=1
            else:
                ans = max(ans,curr)
                curr=0
        ans = max(ans,curr)
        return ans
        