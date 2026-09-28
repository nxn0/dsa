class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
       b=sum(a==b for a, b in pairwise(nums))
       g=Counter((min(a,b),max(a,b)) for a,b in pairwise(nums)if a!=b)
       return b+max(g.values(),default=0)