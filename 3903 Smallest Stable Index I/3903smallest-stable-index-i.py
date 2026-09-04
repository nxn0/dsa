class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        return  next((i 
            for i,(mx,mn) in enumerate(zip(accumulate(nums, max),
                                         [*accumulate(nums[::-1], min)][::-1])) 
            if  mx-mn <=k
        ), -1)