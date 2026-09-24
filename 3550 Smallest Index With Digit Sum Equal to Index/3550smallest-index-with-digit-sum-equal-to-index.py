class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
       n = len(nums)
    
       for i in range(n):
          x = sum(int(digit) for digit in str(nums[i]))
          if x == i:
              return i
       return -1
          