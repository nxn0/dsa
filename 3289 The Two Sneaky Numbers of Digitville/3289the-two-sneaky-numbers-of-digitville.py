class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        a,b = 0,0
        n= sorted(nums)
        for i in range(len(nums)-1):
            a = n[i]
            b = n[i+1]
            if a == b: 
                ans.append(a)
        return ans



