

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos  = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        a = 0
        for x, dic in pos.items():
            if len(dic) == 3:
                if dic[1]-dic[0] == dic[2]-dic[1]:
                    a+=1
                
        return a
        