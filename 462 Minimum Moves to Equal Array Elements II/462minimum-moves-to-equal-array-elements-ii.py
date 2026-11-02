class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = sorted(nums)
        o = int(len(n)/2)
        mid = n[o]
        a = 0
        for i in n:
            a += abs(i-mid)
        return a