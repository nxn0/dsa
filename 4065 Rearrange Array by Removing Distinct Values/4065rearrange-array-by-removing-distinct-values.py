class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        res,rem = [],[]
        while nums:
            for i,x in enumerate(nums):
                if i==0 or x!=nums[i-1]:
                    res.append(x)
                else:
                    rem.append(x)
            nums,rem=rem,[]
        return res
        