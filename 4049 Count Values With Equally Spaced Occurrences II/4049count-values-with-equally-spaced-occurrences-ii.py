class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        p = defaultdict(list)
        for i, x in enumerate(nums):
            p[x].append(i)
        ans = 0
        for x, bleh in p.items():
            if len(bleh) >=3:
                # ik for fucks ske its im - i[m-1] hoe tf i implement t
                lala = bleh[1]-bleh[0]
                if all(bleh[i]-bleh[i-1] == lala for i in range(2, len(bleh))):
                    ans+=1
        return ans
                